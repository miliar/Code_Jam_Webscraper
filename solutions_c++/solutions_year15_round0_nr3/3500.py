#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int find_j( const int rep, const string str, const int sub, int sign,
	    char str_result, int str_sign );
int find_k( const int rep, const string str, const int sub, int sign,
	    char str_result, int str_sign );


char mul( const char a, const char b, int *sign )
{
  if ( a == '1' )
    return b;
  if ( b == '1' )
    return a;

  if ( a == 'i' ) {
    if ( b == 'i' ) {
      *sign *= -1;
      return '1';
    }else if ( b == 'j' ) {
      return 'k';
    } else if ( b == 'k' ) {
      *sign *= -1;
      return 'j';
    }
  } else if ( a == 'j' ) {
    if ( b == 'i' ) {
      *sign *= -1;
      return 'k';
    } else if ( b == 'j' ) {
      *sign *= -1;
      return '1';
    } else if ( b == 'k' ) {
      return 'i';
    }
  } else if ( a == 'k' ) {
    if ( b == 'i' ) {
      return 'j';
    } else if ( b == 'j' ) {
      *sign *= -1;
      return 'i';
    } else if ( b == 'k' ) {
      *sign *= -1;
      return '1';
    }
  }
}

int judge( const int rep, const string str )
{
  char str_result = '1';
  int str_sign = 1;

  for ( int i = 0; i < str.length(); i++ )
    str_result = mul( str_result, str[ i ], &str_sign );

  char t_re = '1';
  int t_si = 1;
  for ( int i = 0; i < rep; i++ ) {
    t_si *= str_sign;
    t_re = mul( t_re, str_result, &t_si );
  }
  
  if ( t_re == '1' && t_si == -1 ) {
    int sign = 1;
    char result = '1';

    for ( int i = 0; i < str.length()*rep; i++ ) {
      result = mul( result, str[ i%str.length() ], &sign );
      if ( result == 'i' )
	if ( find_j( rep, str, i, sign, str_result, str_sign ) )
	  return 1;
    }
    return 0;
  } else
    //    cout << endl << t_re << " " << t_si << endl << endl;
    return 0;
}

int find_j( const int rep, const string str, const int sub, int sign,
	    char str_result, int str_sign
	    )
{
  char result = '1';

  for ( int i = sub+1; i < str.length()*rep; i++ ) {
    result = mul( result, str[ i%str.length() ], &sign );
    if ( result == 'j' )
      if ( find_k( rep, str, i, sign, str_result, str_sign ) )
	return 1;
  }
  return 0;
}

int find_k( const int rep, const string str, const int sub, int sign,
	    char str_result, int str_sign )
{

  int result = 1;
  int rep_k;

  for ( int i = sub+1; i < str.length()*rep; i++ ) {
    result = mul( result, str[ i%str.length() ], &sign );
    if ( (i+1)%str.length() == 0 ) {
      rep_k = rep - (i+1)/str.length();
      break;
    }
  }

  while ( rep_k-- > 0 ) {
    sign *= str_sign;
    result = mul( result, str_result, &sign );
  }

  if ( result == 'k' && sign == 1 )
    return 1;
  else
    return 0;
}

int main()
{
  ifstream fin( "input/C-small-attempt1.in.txt" );
  ofstream fout( "output/output" );
  cin.rdbuf( fin.rdbuf() );
  cout.rdbuf( fout.rdbuf() );

 int case_num;
 cin >> case_num;

 for ( int i = 1; i <= case_num; i++ ) {
    string str;
    int rep, len;
    cin >> len >> rep >> str;

    cout << "Case #" << i << ": ";
    if ( judge( rep, str ) )
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
     }

  return 0;
}
