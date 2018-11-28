// reading a text file
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <cmath>

using namespace std;

//if isprime == 0, then prime
int IS_prime(unsigned long long int num)
{
  //Note that I could use this formula to find list of prime and then compare with value, but i used list of prime
  unsigned long long int isprime = 0;
  for(unsigned long long int i = 2; i*i <= num; i++)
  {
    if(num%i == 0)
    {
      isprime = i;
      break;
    }
  }

  return isprime;
}

unsigned long long int interpretation(int base, int N, char* value){
  unsigned long long int result = 0;
  int int_value=0;
  for(unsigned long long int i=0,j=N-1;i<N;i++,j--){
    if(value[i]=='0')
      int_value=0;
    else
      int_value=1;
    result = result + int_value*pow(base,j);
  }
  //cout << result <<endl;
  return result;
}

int main() {
  string line;
  ifstream myfile ("c.txt");
  ofstream outfile ("C_out.txt");
  if (myfile.is_open() && outfile.is_open())
  {
  	getline(myfile,line);
  	istringstream buffer(line);
  	int size;
  	int answer;
    int N;
    int J;
  	buffer >> size;
    int whitespaceindex = 0;
  	for(int i=1; i<=size; i++){
  		getline(myfile,line);
      buffer.str(line);
      buffer >> N;
      buffer >> J;
      unsigned long long int result[J][11];
      int J_index = 0;
      char value[N];
      outfile << "Case #" << i <<":" << endl;
      for(int k = 0; k < pow(2,N-2) ;k++){
        value[0]='1';
        value[N-1]='1';
        int tmp=k;
        for(int l=N-2; l>0;l--){
          if(tmp%2==0)
            value[l] = '0';
          else
            value[l] = '1';
          tmp /= 2;
        }
        // base 2 to 10
        for(int m=2; m <=10; m++){
          result[J_index][m] = interpretation(m,N,value);
          int divisor = IS_prime(result[J_index][m]);
          if(divisor==0){
            //cout<< "this is a prime" << endl;
            break;
          } else {
            //cout << "this is not a prime" <<endl;
            //update with divisor
            result[J_index][m] = divisor;
            //cout << "divisor =" << result[J_index][m] << endl;
            
            if(m == 10){
              //cout << "Find jamcoin : ";
              //print write to file with answer
              for(int o=0; o<N; o++){
                outfile << value[o];
              }
              outfile << " ";

              for(int p=2;p<=10;p++){
                outfile << result[J_index][p];
                if(p != 10)
                  outfile << " ";
                else
                  outfile << endl;
              }

              J_index++;
            }
          }
        }
        if(J_index == J){
          cout << "find all jamcoin\n"; 
          break;
        }
      }
  	}
    myfile.close();
    outfile.close();
  }

  else cout << "Unable to open file"; 

  cout << "done\n" <<endl;
  return 0;
}
