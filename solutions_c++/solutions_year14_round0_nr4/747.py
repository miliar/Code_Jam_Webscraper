#include <cstdlib>
#include <math.h>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

    long double  A[1000], B[1000];
    long double  AA[1000], BB[1000], CC[1000];
    int XA[1000], XB[1000], XC[1000]; 
	int N;
	int curr;
	long double lastmin, BB_min, BB_max;
	int X,Y;
	int I_min, I_max, II_min, II_max;
	string temp;
	int ddigits;
	int digit_m;
    for (int T_i=0; T_i<T;T_i++){
        cin >> N;
        for (int i =0; i< N; i ++){
            cin.precision(7);
            cin >> temp;
            A[i] = atof(temp.c_str());
            XA[i]=0;
        }
        ddigits = temp.length()-2;
        digit_m = 1;
        for (int i=0; i<ddigits;i++) digit_m= digit_m* 10;
        for (int i =0; i< N; i ++){
            cin.precision(7);
            cin >> B[i];
            XB[i]=0;
            XC[i]=0;
        }
        AA[0]=0;
        for (int a=0; a< N; a ++){
            lastmin = 10;
//            if (a >0) AA[a] = AA[a-1];
            for (int b=0; b<N; b++){
                if ((AA[a] < A[b]) && (A[b] < lastmin)) lastmin = A[b];
            }
            if (a<N-1) AA[a+1] = lastmin;
            AA[a] = lastmin * digit_m;
            CC[a] = AA[a];
        }

        BB[0]=0;
        for (int a=0; a< N; a ++){
            lastmin = 10;
 //           if (a >0) BB[a] = BB[a-1];
            for (int b=0; b<N; b++){
                if ((BB[a] < B[b]) && (B[b] < lastmin)) lastmin = B[b];
            }
            if (a<N-1) BB[a+1] = lastmin;
            BB[a] = lastmin * digit_m;
        }

//        for (int a=0; a<N; a++) {
//            cout << AA[a] << " ";
//        }
//        cout << endl;
//        for (int a=0; a<N; a++) {
//            cout << BB[a] << " ";
//        }
//        cout << endl;

        X=0;
        Y=0;
        
        I_min = 0; 
        II_min = 0;
        I_max = N-1;
        II_max = N-1;
        
        int duplfound, t_II_max, t_II_min;
        long double temp_Max;
        for (int a=0; a<N; a++) {
            if (AA[I_min] < BB[II_min]) {
                
                duplfound = 1;          
                temp_Max = BB[II_max];
                while (duplfound==0) {
                duplfound=0;
                temp_Max--;
                for (int c=0; c<N; c++){
                    if (CC[c] == temp_Max) duplfound = 1;
                    if (BB[c] == temp_Max) duplfound = 1;
                }
                } 
                
                if (temp_Max <= 0) temp_Max = AA[I_min];
                t_II_max = II_max;
                while ((t_II_max > 0) && ((BB[t_II_max] < temp_Max) || XA[t_II_max]==1)) t_II_max--;
                t_II_max ++;
                XA[t_II_max] = 1;
                if (t_II_max == II_max) while (XA[II_max]==1) II_max--;
                CC[I_min] = temp_Max;
                I_min++;
                
                      } else {
                      if (AA[I_min] > BB[II_min]) {
                                    
                           temp_Max = digit_m;  
                           while ((temp_Max > AA[I_min]) && (duplfound==0)) {
                                    duplfound=0;
                                    temp_Max --;
                                    for (int c=0; c<N; c++){
                                        if (CC[c] == temp_Max) duplfound = 1;
                                        if (BB[c] == temp_Max) duplfound = 1;
                                    }
                                 }
                           CC[I_min] = temp_Max;
                           XA[II_min] = 1;    
                           while (XA[II_min]==1) II_min++;
                           I_min++;
                           X++;
                                    }
                             
                      }
        }

        I_min = 0; 
        II_min = 0;
        I_max = N-1;
        II_max = N-1;

        for (int a=0; a<N; a++) {
            if (AA[I_min] < BB[II_min]) {
                XB[II_min] = 1;
                while (XB[II_min]==1) II_min ++;
                I_min++;
                      } else {
                        t_II_min= II_min;
                        while ((t_II_min < N) && ((AA[I_min] > BB[t_II_min]) || (XB[t_II_min]==1))) t_II_min++;
                        if (t_II_min < N) {
                           XB[t_II_min] = 1;
                           I_min++;
                           if (t_II_min == II_min) while (XB[II_min]==1) II_min ++; }
                        else {
                           Y++;
                           I_min++;
                           XB[II_min] = 1;
                           while (XB[II_min]==1) II_min ++;
                           }
                      }
        }

        
        cout << "Case #" << T_i+1 << ": "  << X << " " << Y << endl;
        
        
    }
    
    return EXIT_SUCCESS;
}
