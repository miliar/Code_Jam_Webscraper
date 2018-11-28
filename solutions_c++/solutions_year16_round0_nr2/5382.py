#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;
typedef long long LL;


int main()
{
    int tries;
    string N;
    FILE *fin = freopen("B-large.in", "r", stdin);
    assert(fin!=NULL );
    FILE *fout = freopen("B-large.out", "w", stdout);
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        cin >> N;
        int flips = 0;
        char *arr = new char[N.length()+1];
        strcpy(arr,N.c_str());
        int count_plus(0),point_neg(0),count_minus(0),point_pos(0);
        for(int j=0;j<N.length();j++){
            if(arr[j]=='+'){
                count_plus++;
            }
            else{
                count_minus++;
            }
        }
        if(count_plus==N.length()){
            cout << "Case #" << i <<": "<< "0" << endl;
        }
        else if(count_minus==N.length()){
            cout << "Case #" << i<<": " << "1" << endl;
        }
        else{
            while(count_minus>0){
                bool first_pos;
                if(arr[0]=='+'){
                    first_pos = true;
                }
                else{
                    first_pos = false;
                }
                if(first_pos){
                    for(int l =0;l<=N.length();l++){
                        point_pos++;
                        if(arr[l+1]=='-'){
                            break;
                        }
                    }
                    for(int l =0;l<=point_pos;l++){
                        arr[l] = '-';
                    }
                    flips++;
                }
                else{
                    point_neg = N.length()-1;;
                    for(int l=N.length()-1;l>=0;l--){
                        if(arr[l]== '-'){
                            point_neg = l;
                            break;
                        }
                    }
                    flips++;
                    char *arr1 = new char[point_neg+1];
                    for (int l = 0; l<=point_neg; l++)
                        arr1[point_neg-l] = arr[l];
                    for(int l=0;l<=point_neg;l++){
                        if (arr1[l] == '+')
                            arr[l] = '-';
                        else
                            arr[l] = '+';
                    }
                }
                point_neg = 0;
                point_pos = 0;
                count_minus=0;
                for(int l =0;l<=N.length();l++){
                    if(arr[l] == '-')
                        count_minus++;
                }
            }
            cout << "Case #" <<i <<": "<<flips << endl;
        }

    }
    return 0;

}
