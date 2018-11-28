#include<iostream>
#include<set>
#include<fstream>
#define ll long long
using namespace std;

int main(){
ifstream input("A-large.in");
ofstream out("ASmallOut.txt");
ll  T , n , c;
input >> T;
set<int> s;
for(int t = 1; t <= T ; t++){
s.clear();
input >> n;
if(n==0) {out <<"Case #" << t << ": " << "INSOMNIA" << endl; continue;}
for(int i= 1; ; i++){

 for(c = n*i ; c ; c/=10)
   s.insert(c%10);

 if(s.size()==10) {out <<"Case #" << t << ": " << n*i << endl; break;}

}
if(t==80) cout << n << endl;
}
input.close();
out.close();
return 0;
}
