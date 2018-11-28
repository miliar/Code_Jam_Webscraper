#include <bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int cases; cin >> cases;
    for(int ii=1;ii<=cases;ii++)
    {


        int max1,c1,finalc=0;
        int current=0,need;
        cin >> max1;
        string s1;
        cin >> s1; int z=s1.size();
        if(z==1){if(max1==0)finalc=0;
                else{
                    if(max1>s1[0]-48){finalc=max1-s1[0]-48;}
                    else{finalc=0;}
                }
                }
        else
        {

        current+=s1[0]-48;
        for(int i=1;i<z;i++)
        {

            if(i>current)
            {
                int temp=i-current;
                finalc+=temp;
                current+=temp;
                current+=s1[i]-48;
            }
            else
            {
                current+=s1[i]-48;
            }
        }
        if(max1>current){finalc+=max1-current;}
        }



cout << "Case #"<<ii<<": ";
    cout << finalc;
    if(ii!=cases){cout << endl;}
    }







}
