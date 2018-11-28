#include <cstdlib>
#include <math.h>
#include <iostream>

using namespace std;

string squarestr(string a){
    string t1,t2,t3;
    int h = a.length();
    t1 = "";
    int d;
    int extra_d;
    char aa,bb;
    for (int i=0; i < h;i++){
        t2="";
        for (int j=0; j < h; j ++ ){
            t2 = t2 + (char)(((int)((char)a[j])-48 ) * ((int)(char)a[h-i-1]-48)+48) ;
        }        
        
        for (int j=0; j <i; j++){
            t2 = t2 + '0';
        }  
        while (t1.length() < t2.length()) {
                 t1 = '0' + t1;
              }
        t3="";
        
        extra_d = 0;
        for (int j=t2.length()-1;j>=0;j--){
            aa= t2[j];
            bb= t1[j];
            d = (((int)aa)-48) + (((int)bb)-48) + extra_d; 
            extra_d = 0;
            if (d>9) {d=d-10; extra_d = 1;}
            t3= (char)(d+48) + t3;
        }
        t1 = t3;
    }
    return t3;
}


string fixstr(string s, int l){
     while (((char)s[0] =='0') && (s.length()>l) ) {
           s = s.substr(1,100);
           }
     while (s.length() < l) {
           s = '0' + s;
           }
     return s;
       }

bool isfair(string s){
     
     while ((char)s[0] =='0') {
           s = s.substr(1,100);
           }

     int l = s.length();
     int l2 = (int)floor(l/2);
     
     bool fair = true;
     for (int i=0;i < l2;i++){
         if ((char)s[i] != (char)s[l-i-1]) {fair = false; i = l2;}
     }
     return fair;
}


int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    string A,B;
    
    string T1,T2;
    int FairSquare;
    cin >> T;
    for (int t=0; t < T; t++){
        cin >> A >> B;

        int A_len = (int)ceil(A.length()/2.0);
        int B_len = (int)ceil(B.length()/2.0);
        int B_LEN = B.length();

        string S_awal = "1";
        string S_akhir = "";
        for (int i=1; i<A_len; i++) S_awal =  S_awal  + "0";
        S_awal = fixstr(S_awal,B_len);
        S_awal = "0" + S_awal;
        
        A =  fixstr(A,B_LEN);
        
        int dig; 
        int doloop=0;
        
        FairSquare = 0;
        
        if ((A<= fixstr("9", B_LEN)) && (B >= fixstr("9",B_LEN))) FairSquare +=1; 
        while ((char)S_awal[0] == '0') {
                if (isfair(S_awal)) {
                     S_akhir = fixstr(squarestr(S_awal),B_LEN);
                     if ((S_akhir >= A) && (S_akhir <= B)) {
                         if (isfair(S_akhir)) {FairSquare ++; }
                                  }
                                    } 
                dig = B_len;
                doloop = 1;
                while (doloop == 1){
                if ((char)S_awal[dig] == '0') {S_awal[dig] = '1'; doloop = 0;}
                else if ((char)S_awal[dig] == '1') {S_awal[dig] = '2';doloop = 0;}
                else if ((char)S_awal[dig] == '2') {
                     S_awal[dig] = '0';
                     dig --;
                     doloop = 1;
                     if (dig<0) doloop = 0;
                }
                } ; 
        }
        
        
        cout << "Case #" << (t+1) << ": " << FairSquare << endl;
        
    }
        
    return EXIT_SUCCESS;
}
