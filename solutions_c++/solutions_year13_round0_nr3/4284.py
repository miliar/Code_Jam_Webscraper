#include<iostream>
#include<sstream>
using namespace std;
bool isPalindrome(long long x)
{
    stringstream s;
    s << x;
    string h = s.str();
    int i,len = h.length()-1;
    for(i=0;i<h.length()/2;i++)
        if(h[i] != h[len--]) 
            return false;
    return true;
}
int main()
{
    long long i,arr[1101],j,upper,lower,;
    int n,m=0,low,high;
    for(i=1;i<10000001;i++)
    {
        if(isPalindrome(i*i) && isPalindrome(i)) arr[m++] = i*i;
    }
    cin>>n;
    for(i=0;i<n;i++)
    {
        high = low =0;
        cin>>lower>>upper;
        for(j=0;j<m;j++) if(arr[j] > lower) { low=j;break;}
        for(j=0;j<m;j++) if(arr[j] <= upper) high=j;
        for(j=0;j<m;j++) if(arr[j]==lower) {low = j;break;}
        for(j=0;j<m;j++) if(arr[j]==upper) {high = j;break;}
        cout << "Case #" << i+1 << ": " << high-low + 1 <<endl;
    }
    return 0;
}
        
