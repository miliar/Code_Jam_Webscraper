#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i,si;
    string s;
    fstream fp;
    fp.open("A-large.in",ios::in);
    ofstream fo;
    fo.open("out.txt",ios::out);
    int w[10];
    int a[26];

    fp>>t;

    for(int q=0;q<t;q++)
    {
        fp>>s;

        si=0;
        for(i=0;i<10;i++)
        {
            w[i]=0;
        }
        for(i=0;i<26;i++)
        {
            a[i]=0;
        }
        for(i=0;i<s.length();i++)
        {
            a[s[i]-65]+=1;
            //cout<<s[i]-64;
            si+=1;
        }
       while(si>0)
        {
            if(a[25]&&a[4]&&a[17]&&a[14])
            {
                a[25]--;
                a[17]--;
                a[4]--;
                a[14]--;
                w[0]++;
                si-=4;
            }
            else if(a[18]&&a[8]&&a[23])
            {
                a[18]--;
                a[8]--;
                a[23]--;
                w[6]++;
                si-=3;
            }
            else if(a[19]&&a[22]&&a[14])
            {
                a[19]--;
                a[22]--;
                a[14]--;
                w[2]++;
                si-=3;
            }
            else if(a[4]&&a[8]&&a[6]&&a[7]&&a[19])
            {
                a[4]--;
                a[6]--;
                a[8]--;
                a[7]--;
                a[19]--;
                w[8]++;
                si-=5;
            }
            else if(a[5]&&a[14]&&a[20]&&a[17])
            {
                a[5]--;
                a[14]--;
                a[20]--;
                a[17]--;
                w[4]++;
                si-=4;
            }
            else if(a[5]&&a[8]&&a[21]&&a[4])
            {
                a[5]--;
                a[8]--;
                a[21]--;
                a[4]--;
                w[5]++;
                si-=4;
            }
            else if(a[19]&&a[7]&&a[17]&&(a[4]-1>0))
            {
                a[19]--;
                a[7]--;
                a[17]--;
                a[4]-=2;
                w[3]++;
                si-=5;
            }





            else if(a[18]&&(a[4]-1>0)&&a[21]&&a[13])
            {
                a[18]--;
                a[4]-=2;
                a[21]--;
                a[13]--;
                w[7]++;
                si-=5;
            }
            else if((a[13]-1>0)&&a[8]&&a[4])
            {
                a[13]-=2;
                a[8]--;
                a[4]--;
                w[9]++;
                si-=4;
            }
            else if(a[14]&&a[13]&&a[4])
            {
                a[14]--;
                a[13]--;
                a[4]--;
                w[1]++;
                si-=3;
            }
            else
            {
                cout<<"Not Possible";
            }
        }
        fo<<"Case #"<<q+1<<": ";
        for(i=0;i<10;i++)
        {
            while(w[i]--)
                fo<<i;
        }
        fo<<endl;
    }
}
