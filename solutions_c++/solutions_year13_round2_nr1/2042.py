#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
#define max 1000005

int A,N,x;
int m[max];

int main()
{
    int t,tc;
    int ans1,ans2,ans;
    cin>>tc;
    for(t=1; t<=tc; t++)
    {
        cin>>A>>N;
        for(int i=0; i<N; i++)
            cin>>m[i];

        sort(m,m+N);
        int op=0;
        if(A==1)
            ans = N;
        else
        {
            int currA=A;
            for(int i=0; i<N; i++)
            {
                if(currA>m[i])
                    currA += m[i];
                else
                {
                    if(currA == m[i] && currA == 1)
                    {
                        op+=N-i;
                        break;
                    }
                    else
                    {
                        int temp,j;
                        temp = currA;
                        j=0;
                        while(1)
                        {
                            temp = temp + temp - 1;
                            j++;
                            if(temp >m[i])
                                break;
                        }
                        if(j>1)
                        {
                            op++;
                        }
                        else
                        {
                            currA = temp;
                            currA += m[i];
                            op+=j;
                        }
                    }
                }
            }
            ans1 = op;
            op = 0;
            currA = A;
            for(int i=0; i<N; i++)
            {
                if(currA>m[i])
                    currA += m[i];
                else
                {
                    if(currA == m[i] && currA == 1)
                    {
                        op+=N-i;
                        break;
                    }
                    else
                    {
                        int temp,j;
                        temp = currA;
                        j=0;
                        while(1)
                        {
                            temp = temp + temp - 1;
                            j++;
                            if(temp >m[i])
                                break;
                        }

                        {
                            currA = temp;
                            currA += m[i];
                            op+=j;
                        }
                    }
                }
            }
            ans2 = op;
            if(ans1 < ans2)
                ans = ans1;
            else
                ans = ans2;
            //printf("\n ans1 %d ans2 %d",ans1,ans2);
        }

        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
