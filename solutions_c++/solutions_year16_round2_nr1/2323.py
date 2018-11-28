#include <fstream>
#include <sstream>
#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>
#include <iomanip>
#include <map>
#include <set>
#include <queue>
#include <cmath>

using namespace std;

int E,F,G,H,I,N,O,R,S,T,U,V,W,X,Z;

int main()
{
	ifstream ifs("A-large (9).in");
    ofstream ofs("answer_large_A");
	int Tt;
	ifs >> Tt; cout << "T= " << Tt <<endl;
   
   for(int t=0;t<Tt;t++){  // test cases
	string STR;
    ifs >> STR; 
	//cout << "S= " << STR << endl; 

   E=0; F=0; G=0; H=0; I=0; N=0; O=0;R=0; S=0; T=0; U=0; V=0;W=0;X=0; Z=0;

   for(int i=0;i<int(STR.size());i++){
	   string str=STR.substr(i,1);
	   if(str=="E"){E++;}
	   else if(str=="F"){F++;}
	   else if(str=="G"){G++;}
	   else if(str=="H"){H++;}
	   else if(str=="I"){I++;}
	   else if(str=="N"){N++;}
	   else if(str=="O"){O++;}
	   else if(str=="R"){R++;}
	   else if(str=="S"){S++;}
	   else if(str=="T"){T++;}
	   else if(str=="U"){U++;}
	   else if(str=="V"){V++;}
	   else if(str=="W"){W++;}
	   else if(str=="X"){X++;}
	   else if(str=="Z"){Z++;}
   }

    vector<int>Vec;

	if(W!=0){ for(int i=0;i<W;i++){Vec.push_back(2);}  T-=W; O-=W; W=0;} //2
	if(G!=0){ for(int i=0;i<G;i++){Vec.push_back(8);}  E-=G; I-=G; H-= G; T-=G; G=0;} //8
	if(X!=0){ for(int i=0;i<X;i++){Vec.push_back(6);}  S-=X; I-=X; X=0;} // 6
	if(Z!=0){ for(int i=0;i<Z;i++){Vec.push_back(0);}  E-=Z; R-=Z; O-=Z; Z=0;} //0
	if(U!=0){ for(int i=0;i<U;i++){Vec.push_back(4);}  F-=U; O-=U; R-=U; U=0;} // 4
	if(F!=0){ for(int i=0;i<F;i++){Vec.push_back(5);}  I-=F; V-=F;  F=0;}  //5
	if(V!=0){ for(int i=0;i<V;i++){Vec.push_back(7);}  S-=V; E-=2*V;N-=V; V=0; } //7
	if(R!=0){ for(int i=0;i<R;i++){Vec.push_back(3);}  T-=R; H-=R; E-=2*R; R=0;} // 3
	if(I!=0){ for(int i=0;i<I;i++){Vec.push_back(9);}  N-=2*I; E-=I; I=0;} //9
	if(O!=0){ for(int i=0;i<O;i++){Vec.push_back(1);}  N-=O; E-= O; O=0;} // 1

	sort(Vec.begin(),Vec.end());

	cout << "Case #" <<t+1<<": ";
    ofs << "Case #" <<t+1<<": " ;

	for(int i=0;i<int(Vec.size());i++){
        cout<<Vec[i];
		ofs<<Vec[i];
	}
	cout<<endl;
	ofs<<endl;

   } // end of test cases

 return 0;
}