#include<iostream>
using namespace std;
int main()
{
    int T,i,j,t1=1,Sm,start,res=0,v;
    char S[1000];
    cin >> T;
    while(T--)
    {
        cin >> Sm;
        cin >> S;
        res=0;
        start=S[0]-48;
        for(i=1;i<=Sm;i++)
        {
            v=S[i]-48;
            if(v!=0)
            {


            if(i >start)
            {
                res=res+i-start;
                start=start+v+res;
            }
            else
            {
                start=start + v;
            }
            }

        }

        cout << "Case #" << t1 <<": " << res << endl;
        t1++;

    }

    return 0;
}
