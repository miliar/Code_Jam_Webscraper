#include<iostream>
using namespace std;
int main()
{
    int q,w1,w2,flag,ans,i,j;
    cin >> q;
    for(int t=1;t<q+1;t++)
    {
        cin >> w1;
        flag=0;
        ans=-1;
        int possible[4];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                int s;
                cin >> s;
                if(i==w1-1)
                {
                    possible[j]=s;
                }
            }
        }
        cin >> w2;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                int s;
                cin >> s;
                if(i==w2-1)
                {
                    for(int k=0;k<4;k++)
                    {
                        if(possible[k]==s)
                        {
                            if(flag==0)
                            {
                                flag=1;
                                ans=s;
                            }
                            else if(flag==1)
                            {
                                flag=2;
                            }
                        }
                    }
                }
            }
        }
        cout << "Case #" << t<<": ";
        if(flag==0)
            cout << "Volunteer cheated!" << endl;
        if(flag==1)
            cout << ans << endl;
        if(flag==2)
            cout << "Bad magician!" << endl;
    }


}
