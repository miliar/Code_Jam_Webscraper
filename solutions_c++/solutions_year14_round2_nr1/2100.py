#include<cstdio>
#include<cstring>
#include<iostream>
#include<cstdlib>
using namespace std;
int main()
{
	int t,n,tc=1;
	cin>>t;
	string s[101];
	while(t--)
	{
		int ans=0,i,j,k,l,c1,c2,flag=0;
		cin>>n;
		for(i=0;i<n;i++)
        cin>>s[i];
        //string str=NULL;
            for(i=0,k=0;i<s[0].length() && k<s[1].length();)
            {
                if(s[0][i]!= s[1][k])
                {
                    flag=1;
                    break;
                }
                //str+=s[0][i];
                j=i,c1=c2=0;
                for(;s[0][j]==s[0][i];i++){
                    c1++;
                }
                l=k;
                for(;s[1][k]==s[1][l];k++)
                    c2++;
                ans+=(c1-c2>0 ? c1-c2:c2-c1);
            }
        /*int p;

        for(p=2;p<n;p++){
            string str1='\0';
            for(int i=0;i<s[p].length();i++){
                int j=i;
                str1+=s[p][i];
                for(;s[p][j]==s[p][i];i++){
                    c1++;
                }
            }
            if(str1!=str){
                flag=1;
                break;
            }
        }*/
        cout<<"Case #"<<tc<<": ";
		if(flag==0 && i==s[0].length() && k==s[1].length() )
            cout<<ans<<endl;
		else
            cout<<"Fegla Won\n";
        tc++;
    }
	return 0;
}
