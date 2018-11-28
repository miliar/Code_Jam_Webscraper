
/**
 * Michael V. Antosha   (mivael)
 *
 * Michael.Antosha@gmail.com
 *
 * May 2013
 */

#include <iostream>
using std::clog;
using std::endl;
using std::flush;
using std::istream;

#include <string>
using std::string;

// #include <vector>
// using std::vector;

#include <cassert>

#ifdef SMALL_DATASET
const int MAX_NAME_LENGTH = 100;
#endif
//
#ifdef LARGE_DATASET
const int MAX_NAME_LENGTH = 1 * 1000 * 1000;
#endif

const char CH_UNKNOWN   = -1;
const char CH_CONSONANT = 1;
const char CH_VOWEL     = 2;

template <class T>  T BadValue(void)  { assert(false); }
template <> int BadValue(void)  {  return (-1); }

template <class T>
T read(istream& in)
{
   assert(in.good());
   T value;
   if (in >> value)  return value;
   clog << "read<...> failed... returning fake value..." << endl;
   return BadValue<T>();
}

char char_type(const char ch)
{
   assert('a' <= ch  &&  ch <= 'z');
   assert('z' - 'a' + 1 == 5 + 21);
   char type = CH_UNKNOWN;
   switch (ch)
   {
      case 'a':  case 'e':  case 'i':  case 'o':  case 'u':
	 type = CH_VOWEL;
	 break;
      default:
	 type = CH_CONSONANT;
   }
   return type;
}

int calc_nvalue(const string& name, const int L, const int n)
{
   int nvalue = 0;
   assert(L >= 0  &&  size_t(L) == name.size());
   for (int i = 0;  i < L;  ++i)
   {
      for (int j = i + 1;  j <= L;  ++j)
      {
	 assert(j > i);
	 const string sub = name.substr(i, j - i);
	 assert(sub.size() == size_t(j - i));
	 int cons_count = 0;
	 for (int k = 0;  size_t(k) < sub.size();  ++k)
	 {
	    int type = char_type(sub[k]);
	    if (type == CH_CONSONANT)
	    {
	       ++cons_count;
	    }
	    else
	    {
	       assert(type == CH_VOWEL);
	       cons_count = 0;
	    }

	    assert(0 <= cons_count  &&  cons_count <= k + 1);
	    assert(cons_count <= n);
	    if (cons_count == n)  break;

	 }  // go to next char (inside substring)

	 if (cons_count >= n)  ++nvalue;

      }  // try next substring (with the same start pos, but one char
	 // larger)

   }  // go to next group of substrings (shift substring start by one
      // char)

   return nvalue;
}

int main(void)
{
   using std::cin;
   using std::cout;

   clog << "Hello." << endl;

   const int T = read<int>(cin);
   assert(1 <= T  &&  T <= 100);

   for (int tc = 1;  tc <= T;  ++tc)
   {
      clog << "Test case #" << tc << "..." << endl;

      const string name = read<string>(cin);
      const int L = name.size();
      assert(0 < L  &&  L <= MAX_NAME_LENGTH);

      const int n = read<int>(cin);
      assert(0 < n  &&  n <= L);

      const long long max_nvalue = ((long long) L) * (L + 1) / 2;
      assert(max_nvalue * 2 / L == L + 1);

      long long nvalue = -1;

#ifdef SMALL_DATASET
      nvalue = calc_nvalue(name, L, n);
#endif

      assert(0 <= nvalue  &&  nvalue <= max_nvalue);
      cout << "Case #" << tc << ": " << nvalue << endl;
   }

   return 0;
}
