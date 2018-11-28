#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>

using namespace std;

#define OVERFLOW 2
#define ROW b_len
#define COL a_len+b_len+OVERFLOW
int getCarry(int num) {
    int carry = 0;
    if(num>=10) {
        while(num!=0) {
            carry = num %10;
            num = num/10;
        }
    }
    else carry = 0;
    return carry;
}

int num(char a) {
    return int(a)-48;
}

string mult(string a, string b) {
        string ret;
        int a_len = a.length();
        int b_len = b.length();
        int mat[ROW][COL];
        for(int i =0; i<ROW; ++i) {
            for(int j=0; j<COL; ++j) {
                mat[i][j] = 0;

            }
        }

        int carry=0, n,x=a_len-1,y=b_len-1;
        for(int i=0; i<ROW; ++i) {
            x=a_len-1;
            carry = 0;
            for(int j=(COL-1)-i; j>=0; --j) {
                if((x>=0)&&(y>=0))  {
                    n = (num(a[x])*num(b[y]))+carry;
                    mat[i][j] = n%10;
                    carry = getCarry(n);
                }
                else if((x>=-1)&&(y>=-1)) mat[i][j] = carry;
                x=x-1;
            }
            y=y-1;
        }

        carry = 0;
        int sum_arr[COL];
        for(int i =0; i<COL; ++i) sum_arr[i] = 0;
        for(int i=0; i<ROW; ++i) {
            for(int j=COL-1; j>=0; --j) {
                sum_arr[j] += (mat[i][j]);
            }
        }
        int temp;
        for(int i=COL-1; i>=0; --i) {
            sum_arr[i] += carry;
            temp = sum_arr[i];
            sum_arr[i] = sum_arr[i]%10;
            carry = getCarry(temp);
        }

        for(int i=0; i<COL; ++i) {
            ret.push_back(char(sum_arr[i]+48));
        }

        while(ret[0]=='0'){
            ret = ret.substr(1,ret.length()-1);
        }
        return ret;
}


int main( int argc, char** argv){


ofstream output;
ifstream input;
cout<< " start "<<endl;
input.open(argv[1]);
output.open("ans.txt");


if(input.fail()){
  cout<<" error opening file"<<endl;
  return -1;
}


int cases;
input >> cases;

int m;
long long base;
int ary[10];
bool match;
int digit;
string sm;
string sbase;
string ans;
stringstream ss;

for(int i=0; i< cases ; i++){

for(int j=0; j<10 ; j++){
	ary[j]=0;
}
input >> base;
ss.str("");
ss << base;
sbase = ss.str();

cout<<"case "<<i+1<<" "<<sbase<<endl;
if ( base == 0 ){
	output<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;  
	cout<<"Case #"<<i+1<<": "<<"INSOMNIA"<<endl;  
	continue;
}

m=0;
match = 0;
while (!match) {
m++;
ss.str("");
ss << m;
sm.clear();
sm = ss.str();


ans.clear();
ans = mult( sm, sbase ); 


//cout<<"case "<<i+1<<" "<<base<<" current "<<ans<<" sm "<<sm<<" sbase "<<sbase<<endl;

for( int j=0; j < ans.size() ; j++){
  digit = ans[j]-48;
  ary[digit]=1;
}

match=1; 
for(int j=0; j<10 ; j++){
	if(ary[j]==0){
		match=0;
		break;
	}
}
}

output<<"Case #"<<i+1<<": "<<ans<<endl;  
cout<<"Case #"<<i+1<<": "<<ans<<endl;  

}

input.close();
output.close();
return 0;
}
