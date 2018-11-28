#include <iostream>

using namespace std;



int main()
{
   int T; cin >> T;
   for (int a=1;a<=T;a++)
   {
      string num; cin >> num;
      int d=num.length();
      int Z=0,X=0,G=0,S=0,U=0,W=0;
      int O=0, N=0, H=0, F=0;
      for (int b=0;b<d;b++)
      {
	 char c=num.at(b);
	 switch(c){
	    case 'Z' : Z++; O--; break;
	    case 'X' : X++; S--; break;
	    case 'G' : G++; H--; break;
	    case 'S' : S++; break;
	    case 'F' : F++; break;
	    case 'U' : U++; O--; F--; break;
	    case 'W' : W++; O--; break;
	    case 'O' : O++; break;
	    case 'N' : N++; break;
	    case 'H' : H++; break;
	    default: break;
	 }
      }
      //cout << N << "." << S << endl;
      N-=S+O;
      N/=2;
      cout << "Case #" << a << ": ";
      for (Z;Z>0;Z--)
	 cout << '0';
      for (O;O>0;O--)
	 cout << '1';
      for (W;W>0;W--)
	 cout << '2';
      for (H;H>0;H--)
	 cout << '3';
      for (U;U>0;U--)
	 cout << '4';
      for (F;F>0;F--)
	 cout << '5';
      for (X;X>0;X--)
	 cout << '6';
      for (S;S>0;S--)
	 cout << '7';
      for (G;G>0;G--)
	 cout << '8';
      for (N;N>0;N--)
	 cout << '9';
      cout << endl;
	 
   }
}
