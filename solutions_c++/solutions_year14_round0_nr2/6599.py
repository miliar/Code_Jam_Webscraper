#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>

using namespace std;

int main() {
	int cards[17];
	fstream in22("B-large.in");
	fstream out22("B-large.out",ios::trunc | ios::out);
    double time, time2, c,f,x,k;
    int t, i, n;
    in22>>t;
    cout  << fixed << setw(7) << setprecision(8); 
    out22 << fixed << setw(7) << setprecision(8); 
    cout<<t<<' '<<endl;
     for (i=1;i<=t;++i){
       in22>>c>>f>>x;
       cout<<"c="<<c<<" f="<<f<<" x="<<x<<' '<<endl;
       time=0; k=2;
       while ((c/k+x/(k+f))<(x/k)){time+=c/k;k+=f;}
       time+=x/k;       
       out22<<"Case #"<<i<<": "<<time<<endl;
       cout<<"Case #"<<i<<": "<<time<<endl;
    }
      cin.ignore();
      in22.close();
      out22.close();
    return 0;
}
