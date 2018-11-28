#include<bits/stdc++.h>
using namespace std;
int main()
{
	ios::sync_with_stdio(false);
    int t=1,T;
    cin>>T;
    while(t<=T)
    {
        cout<<"Case #"<<t<<": ";
        int n,i,j;
        char s[100][101];
        int compose[100][100][2]={0};
        int cc[100]={0};
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>s[i];
            cc[i]++;
            compose[i][cc[i]-1][0]=s[i][0];
            compose[i][cc[i]-1][1]=1;

            for(j=1;s[i][j]!='\0';j++)
            {
                if(s[i][j]==compose[i][cc[i]-1][0])
                {
                    compose[i][cc[i]-1][1]++;
                }
                else
                {
                    cc[i]++;
                    compose[i][cc[i]-1][0]=s[i][j];
                    compose[i][cc[i]-1][1]=1;
                }
            }

        }
        int flag=1;
        int tcom,moves,red,inc,max,min;
        for(i=1;i<n;i++)
        {
            if(cc[i]!=cc[i-1])
            {
                flag=0;
                goto end;
            }
        }

        tcom=cc[0];
        moves=0;
        //int red,inc,max,min;
        for(i=0;i<tcom;i++)
        {
            red=0;
            inc=0;
            max=compose[0][i][0];
            min=compose[0][i][0];
            char curchar=compose[0][i][0];
            for(j=0;j<n;j++)
            {
                if(curchar!=compose[j][i][0])
                {
                    flag=0;
                    goto end;
                }
                if(compose[j][i][1]>max)
                    max=compose[j][i][1];
                if(compose[j][i][1]<min)
                    min=compose[j][i][1];
            }
            int choice,bestchoice=1,bestcost=101,cost;
            for(choice=min;choice<=max;choice++)
            {
                cost=0;
                for(j=0;j<n;j++)
                {
                    cost+=(abs(choice-compose[j][i][1]));
                }
                if(cost<bestcost)
                    bestcost=cost;
            }
            moves+=bestcost;

        }
        end:
        if(flag==0)
        {
            cout<<"Fegla won"<<endl;
        }
        else
        {
            cout<<moves<<endl;
        }

       /* int flag=1;
        char chi;
        cin>>s[0];
        iter[0]=1;
        chi=s[0][0];
        for(i=1;i<n;i++)
        {
            cin>>s[i];
            iter[i]=1;
            if(s[i][0]!=chi)
                flag=0;
        }
        if(flag=0)
        {
            cout<<"Fegla won"<<endl;
            continue;
        }
        int atnull=0;
        int moves=0;
        while(atnull!=n)
        {
            int countprev=0;
            int freq[26]={0};
            int countunique=0;
            for(i=0;i<n;i++)
            {
                if(s[i][iter[i]]==chi)
                {
                    countprev++;
                }
                freq[s[i][iter[i]]-'a']++;
                if(freq[s[i][iter[i]]-'a']==1)
                    countunique++;
            }
            if(countprev==n)
            {
                for(i=0;i<n;i++)
                {
                    iter[i]++;
                }


            }
            else if(countprev!=0)
            {
                for(i=0;i<n;i++)
                {
                    if(s[i][iter[i]]==chi)
                    {
                        iter[i]++;
                    }
                }

            }
            else if(countprev==0 && countunique==1)
            {
               for(i=0;i<n;i++)
                {
                    iter[i]++;
                }

            }
            else if(countprev==0 && countunique>1)
            {
                flag=0;
                break;
            }

        }
        if(flag==0)
        {
            cout<<"Fegla won"<<endl;
        }
        else
        {
            cout<<moves<<endl;
        }

    */

        t++;
    }
	return 0;
}
