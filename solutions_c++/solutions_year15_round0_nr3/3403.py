#include <iostream>
#include <list>
using namespace std;

struct Q
{
  char c;
  int sign;
  Q(char x)  {c = x; sign = 1;}
  bool operator==(Q & q2)
  {
    return (c == q2.c && sign == q2.sign);
  }
};

void out(Q & q)
{
  if (q.sign == 1)  {cout << "(+";}
  else  {cout << "(-";}
  cout << q.c << ")";
}

void output(const list<Q> & str)
{
  for (Q q : str)
  {
    out(q);
    cout << ' ';
  }
  cout << endl;
}
Q mult(Q a, Q b)
{
  //cout << "mult: ";
  //out(a);
  //cout << ", ";
  //out(b);
  //cout << endl;

  Q ret('e');
  ret.sign = a.sign * b.sign;
  if (a.c == 'e')  {ret.c = b.c;}
  else if (b.c == 'e')  {ret.c = a.c;}
  else if (a.c == b.c)  {ret.c = 'e'; ret.sign *= -1;}

  else if (a.c == 'i' && b.c == 'j')  {ret.c = 'k';}
  else if (a.c == 'i' && b.c == 'k')  {ret.c = 'j'; ret.sign *= -1;}
  else if (a.c == 'j' && b.c == 'i')  {ret.c = 'k'; ret.sign *= -1;}
  else if (a.c == 'j' && b.c == 'k')  {ret.c = 'i';}
  else if (a.c == 'k' && b.c == 'i')  {ret.c = 'j';}
  else if (a.c == 'k' && b.c == 'j')  {ret.c = 'i'; ret.sign *= -1;}
  else  {cout << "error" << endl;}
  //cout << " = ";
  //out(ret);
  //cout << endl;

  return ret;
}

bool reduce_front_to(list<Q> & str, Q d)
{
  if (str.front() == d)  {return true;}
  else if (str.size() < 2)  {return false;}
  else
  {
    Q c1 = str.front();
    str.pop_front();
    Q c2 = str.front();
    str.pop_front();
    Q r = mult(c1, c2);
    str.push_front(r);
    return reduce_front_to(str, d);
  }
}

bool reduce_back_to(list<Q> & str, Q d)
{
  if (str.back() == d)  {return true;}
  //else {cout << "str.back(): "; out(str.back()); cout << "d: "; out(d); cout << endl;}

  if (str.size() < 2)  {return false;}
  else
  {
    Q c1 = str.back();
    str.pop_back();
    Q c2 = str.back();
    str.pop_back();
    Q r = mult(c2, c1);
    str.push_back(r);
    return reduce_back_to(str, d);
  }
}


Q evaluate(const list<Q> & str)
{
  Q res('e');
  for (Q q : str)
  {
    res = mult(res, q);
  }
  return res;
}

bool possible(list<Q> & str)
{
  //output(str);

  Q end('k');
  Q begin('i');
  Q goal('e');
  goal.sign = -1;

  list<Q> bak = str;
  bool first = reduce_back_to(str,end);
  first = first && reduce_front_to(str,begin);
  //output(str);
  //cout << "evaluating... "; Q q = evaluate(str); out(q); cout << endl;
  first = first && (evaluate(str) == goal);
  if (first)  {return true;}
  //cout << "nope" << endl;

  str = bak;

  //try with negatives
  begin.sign = 1;
  end.sign = -1;
  bool second = reduce_back_to(str,end);
  second = second && reduce_front_to(str,begin);
  second = second && (evaluate(str) == goal);
  if (second)  {return true;}

  str = bak;

  begin.sign = -1;
  end.sign = 1;
  bool third = reduce_back_to(str,end);
  third = third && reduce_front_to(str,begin);
  third = third && (evaluate(str) == goal);
  if (third)  {return true;}

  str = bak;

  begin.sign = -1;
  end.sign = -1;
  bool fourth = reduce_back_to(str,end);
  fourth = fourth && reduce_front_to(str,begin);
  fourth = fourth && (evaluate(str) == goal);
  if (fourth)  {return true;}
  return false;
}

void tick(int cs)
{
  list<Q> str;
  int n;
  cin >> n;
  int reps;
  cin >> reps;
  string in;
  cin >> in;
  for (int i=0; i < reps; i++)
  {
    for (char c : in)
    {
      Q q(c);
      str.push_back(c);
    }
  }
  //cout << "Evaluate...";
  //Q q = evaluate(str);
  //out(q);
  //cout << endl;
  cout << "Case #" << cs << ": ";
  if (possible(str))
  {
    cout << "YES" << endl;
  }
  else
  {
    cout << "NO" << endl;
  }
}

int main()
{
  int bign;
  cin >> bign;
  for (int i=0 ;i < bign; i++)
  {
    tick(i+1);
  }
  return 0;
}
