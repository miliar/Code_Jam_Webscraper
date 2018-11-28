#include <iostream>
#include<math.h>
using namespace std;
int palin(int p)
{
    int a[5];
    int i = 0;
    int size = 0;
    while(p/10 != 0)
    {
        //cout << "going into the loop"<<endl;
        a[i++] = p%10;
        p = p/10;
        //cout << p << endl;
    }
    a[i] = p;
    size = i;
    //cout << "size is "<<size<<endl;
    //for(int k=0;k<=size;k++)
        //cout << a[k]<<endl;
    i = 0;
    while(a[i] == a[size-i] && i<=size/2)
        i++;
    //cout << "i is "<<i<<endl;
    if(i >=1 && i==(size/2)+1)
        return 1;
    else 
        return 0;
}
int main()
{
    int A = 0, B = 0;
    int T = 0;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cin >> A;
        cin >> B;
        int count = 0;
        int start = sqrt(A);
        if(start*start!=A)
            start++;
        while((start*start)<=B)
        {
            //cout << "start is "<<start<<endl;
            if(palin(start)==1 && palin(start*start) == 1)
            {
                count ++;
                //cout <<start <<" is a suc"<<endl;
            }
            start++;
        }
        cout << "Case #"<<i+1<<": "<<count<<endl;
    }
}
