#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
using namespace std;
typedef long long LL;

int main()
{
    int tries;
    long long N;
    FILE *fin = freopen("A-large.in", "r", stdin);
    assert( fin!=NULL );
    FILE *fout = freopen("A-large.out", "w", stdout);
    cin >> tries;
    for (int i = 1; i <= tries; i++)
    {
        int count = 0;
        long long temp, temp1;
        bool a(true),b(true),c(true),d(true),e(true),f(true),g(true),h(true),l(true),k(true);
        cin >> N;
        if (N == 0)
            cout << "Case #" << i << ": INSOMNIA" << endl;
        else{
            int j = 1;
            while(count<10){
                temp = j*N;
                temp1 = temp;
                while(temp!=0){
                    int val = temp%10;
                    temp = temp/10;
                    switch(val){
                    case 1:
                        if(a){
                            count++;
                            a = false;
                        }
                        break;
                    case 2:
                        if(b){
                            count++;
                            b = false;
                        }
                        break;
                    case 3:
                        if(c){
                            count++;
                            c = false;
                        }
                        break;
                    case 4:
                        if(d){
                            count++;
                            d = false;
                        }
                        break;
                    case 5:
                        if(e){
                            count++;
                            e = false;
                        }
                        break;
                    case 6:
                        if(f){
                            count++;
                            f = false;
                        }
                        break;
                    case 7:
                        if(g){
                            count++;
                            g = false;
                        }
                        break;
                    case 8:
                        if(h){
                            count++;
                            h = false;
                        }
                        break;
                    case 9:
                        if(l){
                            count++;
                            l = false;
                        }
                        break;
                    case 0:
                        if(k){
                            count++;
                            k = false;
                        }
                        break;

                    }
                }
                j++;
            }
            cout << endl << "Case #" << i << ": " << temp1 << endl;
        }
    }
    return 0;
}
