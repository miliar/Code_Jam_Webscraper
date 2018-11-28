#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
using namespace std;
int main()
{
    int T;
    cin>>T;
    int counter=0;
    while(T--)
    {
        counter++;
    	int n;
    	cin>>n;
        vector <double> v1;
        vector <double> v2;
        for(int i=0;i<n;i++){double temp;cin>>temp;v1.push_back(temp);}
        for(int i=0;i<n;i++){double temp;cin>>temp;v2.push_back(temp);}
        int war=0,dis_war=0;
        int p1=0,p2=0;
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        for(int i=0;i<n;i++){if(v2[p2]>v1[p1]){p1++;p2++;}
        else {p2++;war++;}}
        p2=0;p1=0;
        for(int i=0;i<n;i++){if(v2[p2]<v1[p1]){p1++;p2++;dis_war++;}
        else {p1++;}}
        cout<<"Case #"<<counter<<": ";
        printf("%i %i\n",dis_war,war);
    }
}
