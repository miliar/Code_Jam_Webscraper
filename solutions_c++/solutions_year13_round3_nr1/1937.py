#include<iostream>
#include<map>
#include<math.h>
#include<string.h>
#include<string>

#include<vector>
using namespace std;
long int ans=0,n;
class Sol
{
public:
    void Get(string input, int startIndex)
	{
		int xxx = startIndex;
		string s(1, input[xxx]);
		long int i,l=s.size(),x=0,f=0;
        if(l>=n){
        for(i=0;i<l;i++)
        {
            if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u')
            {
                x++;
                if(x==n)
                {
                    f=1;break;
                }
            }
            else
                x=0;
        }
        if(f==1)
            ans++;}
		while (xxx < input.length())
		{
			xxx++;
			if (xxx == input.length())
				break;
			s += input[xxx];
			long int i,l=s.size(),x=0,f=0;            
            if(l>=n){
            for(i=0;i<l;i++)
            {
              if(s[i]!='a'&&s[i]!='e'&&s[i]!='i'&&s[i]!='o'&&s[i]!='u')
              {  x++;
                if(x==n)
                {
                    f=1;break;
                }
            }
                else
                    x=0;
            }
            if(f==1)
                ans++;
		}
        }
		startIndex++;
		if (startIndex < input.length())
			Get(input, startIndex);
	};
};
int main()
{

 freopen("input.txt","r",stdin);
  freopen("output.in","w",stdout);
    long int t,l,i=1;
    string str;
    cin>>t;
    while(t--)
    { ans=0;
        cin>>str>>n;
    Sol obj;
  obj.Get(str,0);
        cout<<"Case #"<<i<<": "<<ans<<"\n";
        i++;
    }
    return 0;
}
