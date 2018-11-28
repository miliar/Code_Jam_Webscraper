#include <cstdio>
#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
 
inline void fastRead_int(int &x) {
	register int c = getchar_unlocked();
	x = 0;
	for(; (c<48 || c>57); c = getchar_unlocked());
	for(; c>47 && c<58 ; c = getchar_unlocked()) {
	    x = (x<<1) + (x<<3) + c - 48;}};

void mult( char&a, char b, int& sign){
    if( a=='1'){ a = b;}
    else if(a == 'i'){ 
                       if(b =='i'){ a='1'; sign=(2-sign)/2;}
                       else if(b == 'j'){ a='k';}
                       else if( b== 'k'){a ='j'; sign=(2-sign)/2; }}
    else if(a == 'j'){ 
                      if(b =='i'){ a='k'; sign=(2-sign)/2; }
                       else if(b == 'j'){ a='1'; sign=(2-sign)/2; }
                       else if( b== 'k'){a ='i';}}
    else if(a == 'k'){ 
                       if(b =='i'){ a='j';}
                       else if(b == 'j'){ a='i'; sign=(2-sign)/2; }
                       else if( b== 'k'){a ='1'; sign=(2-sign)/2; }}}
            
int solve_it(char* arr, int starting_index, int size, int times, char needed){
    //int sindex = starting_index;
    if(starting_index < size*times){
        int lindex = starting_index+1;
        char totalled_to = arr[starting_index];
        int sign = 0; // 0 for positive and 1 for negative
        while( (lindex < size*times) && ((totalled_to != needed)|| sign != -1)  ){
             mult(totalled_to,arr[(lindex%size)],sign);
             lindex++;
        }
        if( totalled_to == needed){ return lindex;}}
     return -1;}

int main() {
	int tcases,L,X;
	int isi,isj,isk;
  ifstream in("C-small-attempt3.in");
  ofstream out("answer");
	char* arr;
  bool* aseenstillthisi;
  bool* bseenstillthisi;
  //fastRead_int(tcases);
  in >> tcases;
  for(int i =1; i<= tcases;i++){
        isi =0; isj=0; isk=0;
        //fastRead_int(L);
        //fastRead_int(X);
        in >> L >> X;
        // if string given contains all i,j,k or not
        arr =new char[L];
        aseenstillthisi = new bool[L];
        bseenstillthisi = new bool[L];
        for(int j =0;j <L; j++){ //arr[j] = getchar_unlocked(); 
                                  in >> arr[j];
                                  aseenstillthisi[j] = false;
                                  bseenstillthisi[j] = false;
                                if(isi == 0 && arr[j] =='i'){isi=1;}
                                else if(isj == 0 && arr[j] =='j'){isj=1;}
                                else if(isk == 0 && arr[j] =='k'){isk=1;}
                         }

        if( (isi == 1 && isj==1) || (isj == 1 && isk ==1) || (isk ==1 && isi ==1)){
                                char inc_a = arr[0];
                                int signa = 0;
                                int isfound = 0;
                                for(int a= 0; ((a < (L*X-2)) && (isfound==0));){
                                     if( (!aseenstillthisi[a%L]) && (inc_a == 'i' && signa == 0)){
                                          aseenstillthisi[a%L] = true;
                                          //search j starting from a+1
                                          char inc_b = arr[(a+1)%L];
                                          int signb = 0;
                                          for(int b =a+1; (b < (L*X-1) && isfound==0);){
                                              if( (!bseenstillthisi[b%L]) && ((inc_b == 'j') && (signb == 0))){
                                                    //search k starting from b+1
                                                    bseenstillthisi[b%L] = true;
                                                    char inc_c = arr[(b+1)%L];
                                                    int signc = 0;
                                                    int c;
                                                    for(c =b+2; c < L*X; c++){
                                                       // cout << inc_c << "  " << arr[c%L] << "     ";
                                                          mult(inc_c,arr[c%L],signc);  //cout << c << " " << inc_c << " " << signc << endl;
                                                        }
                                                    if( inc_c == 'k' && (signc == 0)){
                                                      //out << a <<" " << b <<" "<< c<<  "  "<< L*X<<endl; 
                                                                isfound = 1;}
                                              }
                                          b++;
                                          mult(inc_b,arr[b%L],signb);
                                          }}
                                    //cout << inc_a << " ";
                                    a++;
                                    mult(inc_a,arr[a%L],signa);
                                    //cout << a <<"  " << inc_a <<endl;
                                }
                                if(isfound == 1){  //printf("Case #%d: %s\n",i,"YES");
                                                    //out << "YES"<< endl; 
                                                out << "Case #" << i << ": YES" << endl;
                                                }
                                else{  //printf("Case #%d: %s\n",i,"NO");
                                         out << "Case #" << i << ": NO" << endl;
                                      }}
        else{ 
          //printf("Case #%d: %s\n",i,"NO");
          //out << "NO" << endl;
          out << "Case #" << i << ": NO" << endl;
        }
        delete []arr;
        //cout << i << endl;
      }
    return 0;
}
	