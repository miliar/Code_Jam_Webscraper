#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;
string a;
int n,res,t;
bool arr[110];
void cambia(int lim)
{
    for (int i=0;i<=lim-i;i++)
    {
        swap(arr[i],arr[lim-i]);
        arr[i]=!arr[i];
        if (lim-i!=i)
        arr[lim-i]=!arr[lim-i];
    }
    res++;
}
int main()
{
    freopen("input.txt","r+",stdin);
    freopen("output.txt","w+",stdout);
    ios::sync_with_stdio(0);
    cin >> t;
    for (int c=1;c<=t;c++)
    {
        res=0;
        cin >> a;
        n=a.length();
        for (int i=0;i<n;i++)
            if (a[i]=='+')
                arr[i]=true;
            else
                arr[i]=false;
        int i=n-1;
        while (i>=0)
        {
            while (i==0|| (i>0 && arr[i-1]==arr[i]))
                i--;
            if (i>0)
            {
                if (arr[i-1]==arr[0])
                    cambia(i-1);
                else
                {
                    int j=0;
                    while (arr[j+1]==arr[j])
                        j++;
                    cambia(j);
                }
            }
        }
        if (arr[0]==false)
            cambia(n-1);
        cout <<"Case #"<<c<<": "<< res;
        if (c<t-1)
            cout <<"\n";
        else
            cout << endl;
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
