#include<bits/stdc++.h>
using namespace std;
string s;
int len;

int check(string str)
{

    for(int start=0 ;start<len ; )
    {
        if(str[start]=='-')
            return 0;
          else start++;  
    }
    return 1;
}
void swap_flip(int tj)
{
    
	int f,r,st;
	char temp;
for(f=0,r=tj ; (f<=tj/2) ;f++,r--)
{
	temp=s[f];
	s[f]=s[r];
	s[r]=temp;
}
for(st=0 ; st<=tj ; st++)
{
	if(s[st]=='+')
		s[st]='-';
	else if(s[st]=='-')
		s[st]='+';
}

}
int main()
{
	int t,c;
	scanf("%d",&t);
	for(int i=1 ; i<=t; i++)
	{
		cin>>s;
		len=s.length();
       
        c=0;
		for(int j=len-1; !check(s) ;)
		{  
			 if( (s[j]=='-')&&(s[0]=='-') )
				{
                    swap_flip(j);
                    //cout<<"changed string:: "<<s<<endl;
                    j=len-1;
                    c+=1;
                }
            else if( (s[j]=='+')&&(s[j+1]=='-')&&(s[0]=='+') )
            {
                swap_flip(j);
                j=len-1;
                c+=1;
            }
            else 
                j--;
			
		}
        //cout<<"string "<<s<<endl;
        cout<<"Case #"<<i<<": "<<c<<endl;
	}
	return 0;
}