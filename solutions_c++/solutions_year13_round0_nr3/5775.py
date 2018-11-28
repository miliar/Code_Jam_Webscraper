#include<iostream>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

static const int max_number = 1000;

vector<int>perfect_palindrome_list;

int main()
{
  unsigned int i;
  for(i=1;i<(max_number/2);i++) {
    unsigned int num,digit,rev=0;
    if((num=i*i) > max_number)
      break;
    while(num!=0) {
      digit=num%10;
      rev=(rev*10)+digit;
      num=num/10;
    }
    if(rev==(i*i)) {
      int num1=i,digit1,rev1=0;
      while(num1!=0) {
	digit1=num1%10;
	rev1=(rev1*10)+digit1;
	num1=num1/10;
      }
      if(rev1==i)
	perfect_palindrome_list.push_back(rev);
    }
  }
  int tc=0,start=0,end=0;
  cin >> tc;
  int tcn=1;
  for(;tc>0;tc--) {
    int count=0;
    cin >> start;
    cin >> end;
    for(i=start;i<=end;i++) {
      if(find(perfect_palindrome_list.begin(),perfect_palindrome_list.end(),i)!=perfect_palindrome_list.end())
	count++;
      
    }
    cout << "Case #" <<tcn<<": "<<count<<endl;
    tcn++;
  }
  return 0;
}
