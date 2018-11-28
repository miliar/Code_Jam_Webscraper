#include <cstdlib>
#include <iostream>

using namespace std;

int A[5][5] = {{0,0,0,0,0},
               {0,1,2,3,4},
               {0,2,-1,4,-3},
               {0,3,-4,-1,2},
               {0,4,3,-2,-1}};
                
int main(int argc, char *argv[])
{
    ios::sync_with_stdio(false);
    int T,check;
    cin >> T;
    for(int i = 1;i<=T;++i){
        check=0;
        int L,X;
        cin >> L;
        cin >> X;
        int length = L*X;
        int B[length], C[length];
        char ch;
        cin >> ch;
        if(ch == 'i') B[0] = 2;
        else if(ch == 'j') B[0] = 3;
        else               B[0] = 4;
        C[0] = B[0];
        for(int j = 1;j<L;++j){
            cin >> ch;
            if(ch == 'i') B[j] = 2;
            else if(ch == 'j') B[j] = 3;
            else               B[j] = 4;
            if(C[j-1] > 0)  C[j] = A[C[j-1]][B[j]];
            else            C[j] = -1* A[-1*C[j-1]][B[j]];
        }
        for(int j = 1;j<X;++j){
            for(int k = 0;k<L;++k){
                B[j*L+k] = B[k];
                if(C[(j*L+k)-1] > 0)   C[j*L+k] = A[C[(j*L+k)-1]][B[k]];
                else               C[j*L+k] = -1* A[-1*C[(j*L+k)-1]][B[k]];
            }
        }   
        int num1, num2,num3;
        for(int j = 1;j<length;++j){
            num1 = C[j-1];
            if(num1 != 2) continue;
            for(int k = j;k<length-1;++k){       
                if(C[j-1] > 0 && C[k] > 0){
                   num2 = -1* A[C[j-1]][C[k]];
                }
                else if(C[j-1] > 0 && C[k] < 0){
                   num2 =  A[C[j-1]][-1*C[k]];
                }
                else if(C[j-1] < 0 && C[k] > 0){
                   num2 = A[-1*C[j-1]][C[k]];
                }
                else if(C[j-1] < 0 && C[k] < 0){
                   num2 = -1* A[-1*C[j-1]][-1*C[k]];
                } 
                if(num2!=3) continue;
                if(C[k] > 0 && C[length-1] > 0){
                   num3 = -1* A[C[k]][C[length-1]];
                }
                else if(C[k] > 0 && C[length-1] < 0){
                   num3 =  A[C[k]][-1*C[length-1]];
                }
                else if(C[k] < 0 && C[length-1] > 0){
                   num3 = A[-1*C[k]][C[length-1]];
                }
                else if(C[k] < 0 && C[length-1] < 0){
                   num3 = -1* A[-1*C[k]][-1*C[length-1]];
                }   
                if(num3 == 4) break;
            } 
            if(num1==2 && num2 == 3 && num3 == 4){
               check = 1;
               break;
            }
        }
        if(check==1) cout << "Case #" << i << ": " << "YES\n";
        else      cout << "Case #" << i << ": " << "NO\n";
    }                         
    return 0;
}
