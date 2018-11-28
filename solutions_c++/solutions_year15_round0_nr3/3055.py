#include <iostream>
#include <string>
using namespace std;

typedef struct Q{
  int a, b, c, d;
} Q;

Q initq(char c)
{
  Q q = {0,0,0,0};
  if(c == 'i')
    {
      q.b = 1;
    }
  if(c == 'j')
    {
      q.c = 1;
    }
  if(c == 'k')
    {
      q.d = 1;
    }
  
  return q;
}

Q calc(Q q, Q q2)
{
  Q q3;

  q3.a = q.a*q2.a - q.b*q2.b - q.c*q2.c - q.d*q2.d;
  q3.b = q.a*q2.b + q.b*q2.a + q.c*q2.d - q.d*q2.c;
  q3.c = q.a*q2.c - q.b*q2.d + q.c*q2.a + q.d*q2.b;
  q3.d = q.a*q2.d + q.b*q2.c - q.c*q2.b + q.d*q2.a;
  return q3;
}

int solve()
{
  int l, x;
  string s, s2;
  
  cin >> l >> x >> s;
  if(l*x < 3)
    {
      return 0;
    }
  s2 = s;
  for(int i = 0; i < x - 1; i++)
    {
      s += s2;
    }
  Q q[10001];
  q[0] = initq(s[0]);
  for(int i = 1; i < s.length(); i++)
    {
      Q q2;
      q2 = initq(s[i]);
      q[i] = calc(q[i-1], q2);
    }
  if(!(q[s.length()-1].a == -1 && q[s.length()-1].b == 0 && q[s.length()-1].c == 0 && q[s.length()-1].d == 0))
    {
      //      cout << "aaa" << endl;
      return 0;
    }
  for(int i = 0; i < s.length(); i++)
    {
      if(!(q[i].a == 0 && q[i].b == 1 && q[i].c == 0 && q[i].d == 0))
	{
	  continue;
	}
      for(int j = i + 1; j < s.length()-1; j++)
	{
	  if(!(q[j].a == 0 && q[j].b == 0 && q[j].c == 0 && q[j].d == 1))
	    {
	      continue;
	    }
	  return 1;
	}
      break;
    }
  return 0;
}

int main()
{
  int t;
  cin >> t;
  for(int i = 0; i < t; i++)
    {
      cout << "Case #" << i+1 << ": ";
      if(solve())
	{
	  cout << "YES" << endl;
	}else{
	cout << "NO" << endl;
      }
    }
  return 0;
}
