#include<stdio.h>
#include<iostream>
using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T,casno,sm,borrow,stand,i;
    char man [1010];
    scanf("%d",&T);
    for(casno=1; casno<=T; casno++)
    {
        cin >> sm >> man;
        stand=0;
        borrow=0;
        for(i=0;i<=sm;i++)
        {
            if(stand>=i)
            {
                stand=stand+(man[i]-48);
            }
            else
            {
                borrow=borrow+(i-stand);
                stand=stand+(i-stand);
                stand=stand+man[i]-48;
            }
        }
        cout << "Case #" <<casno <<": ";
        cout << borrow << endl;

    }

}
