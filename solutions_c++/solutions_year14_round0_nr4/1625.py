#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;
int decietful(vector<double>nemo ,vector<double>kemo);
int optimally(vector<double>keno,vector<double>nemo);
int comp(vector<double>keno,vector<double>nemo,int h){
    int c(0);
for (;c<keno.size();c++){
    if (keno[c]>nemo[h])break;

}
return (c);

}
int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    int t;
    cin >> t;
    for (int c(0);c<t;c++){
        int n;
        cin >> n;
        vector<double>nemo,keno;
        for (int c1(0);c1<n;c1++){double a;cin >> a;nemo.push_back(a);}
        for (int c1(0);c1<n;c1++){double a;cin >> a;keno.push_back(a);}
        cout << "Case #" << c+1 << ": " ;
        if (n==1){if (nemo[0]>keno[0]){cout << "1 1" << endl;continue;}else {cout << "0 0" << endl;continue;} }
cout <<decietful(nemo,keno) << " "<< optimally(keno,nemo) << endl;



    }




    return 0;
}

int optimally(vector<double>keno,vector<double>nemo){
sort(keno.begin(),keno.end());
sort(nemo.begin(),nemo.end());
int nemopo(0);
for (int c(nemo.size()-1);c>=0;c--){if (nemo[c]>keno[keno.size()-1]){nemopo++;keno.erase(keno.begin());} else {keno.erase(keno.begin()+comp(keno,nemo,c));} }
return (nemopo);

}

int decietful(vector<double>nemo,vector<double>keno){
sort(nemo.begin(),nemo.end());
sort(keno.begin(),keno.end());
int hhh(nemo.size());
int nempo(0);
for (int c1(0);c1<hhh;c1++){
        if (nemo.size()==1&&nemo[0]>keno[0])nempo++;
       else  if (nemo[nemo.size()-1]>keno[keno.size()-1]&&nemo[0]>keno[0]){nemo.erase(nemo.begin());keno.erase(keno.begin());nempo++;}
    else if (nemo[nemo.size()-1]>keno[keno.size()-1]&&nemo[0]<keno[0]){nemo.erase(nemo.begin());keno.erase(keno.begin()+keno.size()-1);}
else if (nemo[nemo.size()-1]<keno[keno.size()-1]){nemo.erase(nemo.begin());keno.erase(keno.begin()+keno.size()-1);}
}
return nempo;

}
