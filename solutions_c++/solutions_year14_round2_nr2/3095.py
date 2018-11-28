#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

string DecToBin2(int number)
{
    string result = "";
    do
    {
        if ( (number & 1) == 0 )
            result += "0";
        else
            result += "1";

        number >>= 1;
    } while ( number );

    reverse(result.begin(), result.end());
    return result;
}
int BinToDec(string number)
{
    int result = 0, pow = 1;
    for ( int i = number.length() - 1; i >= 0; --i, pow <<= 1 )
        result += (number[i] - '0') * pow;

    return result;
}

int main(){
    int T,A,B,K,i,len,j,a,b,t1,t2,tmp_len,y;
    string tmp1,tmp2,ans;
    cin >> T;
    for(i = 1 ; i <= T ; ++i){
        cin >> A >> B >> K;
        y = 0;
        len = (A > B)?A:B;
        //cout << "len = " << len << endl;
        string binary[len];
        for(j = 0 ; j < len ; ++j){
            binary[j] = DecToBin2(j);
            //cout << binary[j] << endl;
        }

        for(a = 0 ; a <= A-1 ; a++){
            for(b = 0 ; b <= B-1 ; b++){
                tmp1 = binary[a];
                tmp2 = binary[b];
                t1 = tmp1.length();
                t2 = tmp2.length();
                if(t1 > t2){
                    tmp_len = t1-t2;
                    while(tmp_len--){
                        tmp2 = "0" + tmp2;
                    }
                }else{
                    tmp_len = t2-t1;
                    while(tmp_len--){
                        tmp1 = "0" + tmp1;
                    }
                }
                //cout << tmp1 << " : " << tmp2 << " L = " << tmp1.length() << " ";
                ans = "";
                for(j = 0 ; j < tmp1.length() ; j++){
                    if(tmp1[j] == '1' && tmp2[j] == '1'){
                        ans += "1";
                    }else{
                        ans += "0";
                    }
                }

                //cout << a << "," << b << " ";
                //cout << "Bin = " << ans << " ";
                //cout << "Dec = " << BinToDec(ans) << endl;
                int check = BinToDec(ans);
                if(check < K ){
                    y++;
                }
            }
            //cout << "asdas" << endl;
        }
        cout << "Case #" << i << ": " << y << endl;
    }

    return 0;
}
