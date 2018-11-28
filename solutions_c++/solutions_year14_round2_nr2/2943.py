#include <cstdio>
#include <iostream>
#include <iomanip> 
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
int t, total;
long int answer;
cin>>t;
total=t;
while(t-- && t<=100){
long int a,b,k;
cin>>a>>b>>k;
answer=0;
for(long int i=0;i<a;i++)
for(long int j=0;j<b;j++)
{
if((i&j)<k)
answer++;
}

cout << "Case #" << total-t << ": " << answer<<endl;

}
    return 0;
}
