#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int T,m=0,j=0, i=0,k=0, l;
	char S[100];

	cin>>T;
	int cnt[T];

	for(i=0;i<T;i++)
    {
        cnt[i]=0;
        cin>>S;
        l=strlen(S);

        for(m=0;m<l;m++)
        {
            if(S[m]!='+')
            {
                break;
            }
        }
        if(m==l)
        {
            cnt[i]=0;
            continue;
        }
        if(S=="-")
        {
            cnt[i] = 1;
            continue;
        }
        for(k=0;k<l;k++)
        {
            if(S[k] != S[k+1])
            {
                if(S[0]=='+')
                {
                    for(j=0;j<=k;j++)
                    {
                        S[j]='-';
                    }
                }
                else
                {
                    for(j=0;j<=k;j++)
                    {
                        S[j]='+';
                    }
                }
                cnt[i]++;

                for(m=0;m<l;m++)
                {
                    if(S[m]!='+')
                    {
                        break;
                    }
                }
                if(m==l)
                {
                    break;
                }
            }
        }
    }
    for(i=0;i<T;i++)
    {
        cout<<"Case #"<<i+1<<": "<<cnt[i]<<endl;
    }
}
