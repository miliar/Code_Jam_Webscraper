#include <bits/stdc++.h>
using namespace std;
typedef long long int li;

li ii;

void flap(string &str,li j)
{
    li i;
    for(i=0;i<=j;++i)
        str[i] = (str[i] == '+') ? '-' : '+';
    
}



void fu()
{
	string str;
    cin >> str;
    li j = str.length(),cnt=0;
    j--;
    while(j>=0){
        if(str[j]=='-'){
            flap(str,j);
            cnt++;
        }
        j--;
    }
    cout<<"Case #"<<ii<<": "<<cnt<<endl;
}




int main()
{
	li test;
	cin >> test;
	for(ii = 1; ii<=test;++ii) fu();
}