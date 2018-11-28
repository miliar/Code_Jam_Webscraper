#include<iostream>
#include<cmath>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for (int ii = 1; ii<=t; ii++)
    {
        int n, js;
        cin>>n>>js;
        cout<<"Case #"<<ii<<":\n";
        int a[60][10]={0};
        int b[60][10]={0};
        int cnt = 1;
        
        
        for (int jj = 0; jj < 64; jj++)
        {
           a[cnt][0] =  a[cnt][7] = 1;
            int b2 = 1;
            for(int i = 1; i <= 6; i++)
            {
                a[cnt][i] = (jj&b2)/b2;
                b2 = b2*2;
            }
            int cn2 = 0;
            
            for (int i = 2; i <=10; i++)
            {
                int bz = 1;
                int rz = 0;
                
                bool fl = 0;
                for(int j = 7; j >=0; j--)
                {
                    rz += bz*a[cnt][j];
                    bz = bz*i;
                }
                
                if(rz%2)
                {
                    for(int j = 3; j*j <= rz; j+=2)
                        if(rz%j == 0)
                        {
                            cn2++;
                            b[cnt][cn2] = j;
                            break;
                        }
                }
                else
                {
                    cn2++;
                    b[cnt][cn2] = 2;
                }
            }
            if(cn2 == 9)
                {
                    cnt++;
                }
        }
        cnt--;
        int cn3 = 0, k;
        for (int i = 1; i<cnt; i++)
        {
          if(a[i][8] == 0)
          {
              cn3++;
              a[i][8] = cn3;
            for(int j = i+1; j<=cnt; j++)
            {
                for (k = 1; k<=9; k++)
                 {   
                    if(b[i][k]!=b[j][k])
                    break;
                 }
                if(k > 9)
                {
                    a[j][8] = cn3;
                }
            }
          }
        }
        
        for (int j2 = 1; j2 <= cnt; j2++)
            for (int j1 = j2; j1 <= cnt; j1++)
            {
                if (a[j2][8] == a[j1][8])
                {
                    for (int j = 0; j<=7;j++)
                            cout<<a[j2][j];
                        for (int j = 0; j<=7;j++)
                            cout<<a[j1][j];
                        cout<<' ';
                        for(int j = 1; j <= 9; j++)
                            cout<<b[j2][j]<<' ';
                        cout<<endl;
                    js--;
                    if(js == 0)
                        return 0;
                }
            }
    }
    return 0;
}