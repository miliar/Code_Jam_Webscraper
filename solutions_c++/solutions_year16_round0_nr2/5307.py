#include<bits/stdc++.h>
using namespace std;

int main() 
{
    int x;
    cin>>x;
    for(int no=1;no<=x;no++)
    {
        char a[105];
        cin>>a;
        int flag=-1,flip=0;
        for(int i=strlen(a)-1;i>=0;i--)
        {
            if((a[i]=='+'&& flag==-1) || (a[i]=='-'&& flag==1))
            {}
            
            else if((a[i]=='+'&& flag==1) || (a[i]=='-'&& flag==-1))
            {
                flag=-flag;
                flip++;
            }
        }
        cout<<"Case #"<<no<<": "<<flip<<endl;
    }
	return 0;
}
