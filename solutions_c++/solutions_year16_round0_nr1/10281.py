//vivekmufc

#include<bits/stdc++.h>
#include<string>
using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
#define pb(x)                        push_back(x)
#define endl                         '\n'
#define INF                         (int)1e9
int mod = 1000000007;

#define N        100005
#define INT(c)  ((int)((c) - '0'))
#define CHAR(i) ((char)(i + int('0')))

string func(string s)
{
      string ret;
      int carry = 0;
      for (int i = s.size()-1; i >= 0; --i)
      {
            int x = (s[i]-'0')*2;
            x += carry;
            int rem = x%10;
            ret = (char)( rem + '0') + ret;
            carry = x/10;
      }
      if(carry!=0)
            ret = (char)( carry + '0') + ret;

      return ret;
}

string product(string a, string b)
{
      if(a == "0" || b=="0")
            return "0";
vector<int> result(a.size() + b.size(), 0);
for( int i = a.size() - 1; i >= 0; i-- )
{
for( int j = b.size() - 1; j >= 0; j-- )
{
result[ i + j + 1 ] += ( b[ j ] - '0') * ( a[ i ] - '0' ); //single array to store intermediate values
}
}
for( int i = a.size() + b.size(); i >= 0; i-- ){
if( result[ i ] >= 10 ){
result[ i - 1 ] +=result[ i ] / 10;result[ i ] %= 10;
}
}

int flg = 1;
string ans;
// cout << a << " * " << b << " = ";
for( int i = 0; i < a.size() + b.size(); i++ ){
      if(flg && result[i] == 0)
            continue;
      flg = 0;
      ans += (char)(result[i]+'0');
}
      return ans;
}

int arr[10];
int z;

int add(string s)
{
      for (int i = 0; i < s.size(); ++i)
      {
            if(arr[s[i]-'0'] == 0)
            {
                  arr[s[i] - '0'] = 1;
                  z++;
            }
      }
      if(z == 10)
            return 1;
      return 0;
}

string toString(int x)
{
      string ret;
      while(x!=0)
      {
            int temp = x%10;
            ret = char(temp+'0') + ret;
            x /= 10;
      }
      return ret;
}

string multiply(const string &a, const string &b)
{
            if(a == "0" || b=="0")
            return "0";
  /* initially fill the result string with 0's */
  size_t total_len= a.length() + b.length();
  string result(total_len, '0');

  int num;                                      /* intermediate store */
  int i, j;
  int last_pos_i, last_pos_j, last_pos_k;

  last_pos_i= total_len - 1;

  /* i-loop */
  for (i= b.length() - 1; i >= 0; i --)
  {
    last_pos_j= last_pos_i;

    /* j-loop */
    for (j= a.length() - 1; j >=0; j --)
    {
      last_pos_k= last_pos_j;
      num= INT(a.at(j)) * INT(b.at(i));

      /* k-loop : the actual updation of result string takes place here. */
      while (num)
      {
        num += INT(result.at(last_pos_k));
        result.at(last_pos_k)= CHAR(num % 10);
        /* 'carry' it forward.. 😉 */
        num= num / 10;
        last_pos_k --;
      }

      last_pos_j --;
    }

    last_pos_i --;
  }
      string ans;
      int flg = 1;
      for (int i = 0; i < result.size(); ++i)
      {
            if(flg == 1 && result[i] == '0')
                  continue;
            flg = 0;
            ans += result[i];
      }

  return ans;
}

int main()
{
      std::ios::sync_with_stdio(false);
      freopen("output.txt","w",stdout);
      freopen("input.txt","r",stdin);

      int t;
      int cas = 1;
      cin>>t;
      while(t--)
      {
            string s;
            cin>>s;
            int n = s.size();
            z = 0;
            for (int i = 0; i < 10; ++i)
                  arr[i] = 0;
            int flg = 1;
            string ss = s;
            for (int i = 1; i < 10000; ++i)
            {
                  if(add(ss))
                  {
                        flg = 0;
                        cout<<"Case #"<<cas<<": "<<ss<<endl;
                        break;
                  }
                  else
                  {
                        string temp = toString(i);
                        ss = multiply(s,temp);
                  }
                  // cout<<ss<<endl;
            }
            if(flg)
                  cout<<"Case #"<<cas<<": INSOMNIA"<<endl;
            cas++;
      }
}

