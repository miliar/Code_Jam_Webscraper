#include <iostream>  
#include <cstdio>  
#include <fstream>  
using namespace std;  
double c, f, x, s;  
int judge()  
{  
    double temp = (c/s) + (x/(s+f));  
    if(x/s > temp)  
        return 1;  
    else  
        return 0;  
}  
int main()  
{  
    ifstream cin("D:\\B-large.in");  
    freopen("D:\\B-large.out","w",stdout);  
    int k;  
    cin >> k;   
    for(int times = 1; times <= k; times++)  
    {  
        s= 2.0;  
        double ans = 0;  
        cin >> c >> f >> x;  
        while(judge())  
        {  
            ans += c/s;  
            s += f;  
        }  
        ans += x/s;  
        printf("Case #%d: %.7lf\n",times, ans);  
    }  
    return 0;  
}  
