#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;

const int _digs = 16;
char dd[_digs][_digs] = { '0' };
ofstream oufile;
int SUMM = 0;
int _alen;
int _blen;
string _glba;
string _glbb;

string mltp(string &numString1 ,string &numString2 );

bool ifPalindrome( string(& str) )
{
	bool pali = true;
	int len = str.length();

	for( int i = 0; i <= len / 2 && pali; i++ )
		pali *= (str.substr(i, 1) == str.substr( len - 1 - i, 1 )) ? true : false;

	return pali;
}

bool checkNumbers( string &stst )
{
	if( ifPalindrome(stst) )
	{
		int LLL = stst.length();
		if( LLL > _alen && LLL < _blen )
		{
			SUMM++;
		}
		else if( LLL > _blen )
		{
			return false;
		}
		else
		{
			if( LLL == _alen && LLL == _blen && stst >= _glba && stst <= _glbb )
				SUMM++;
			else if( LLL == _alen && LLL != _blen && stst >= _glba )
				SUMM++;
			else if( LLL != _alen && LLL == _blen && stst <= _glbb )
				SUMM++;
		}
	}
	return true;
}

string intToStr( int k )
{
	stringstream ss;
	ss << k;
	return ss.str();
}

void bigSum( string& strSum, string& str1, string& str2 )
{
	strSum = "";
	str1 += "0";
	str2 += "0";
	int n = str1.length() - str2.length();
	if( n > 0 )
		for( int i = 0; i < n; i++ )
			str2 += "0";
	else
		for( int i = 0; i < -n; i++ )
			str1 += "0";

	string nasht = "0";
	int length = str1.length();
	int from = 0;
	int len = 0;
	int s1 = 0;
	int s2 = 0;
	int sum = 0;

	while( length != 0 )
	{
		len = length > 8 ? 8 : length;
		string s1sub = str1.substr(from, len);
		string s2sub = str2.substr(from, len);

		reverse( s1sub.begin(), s1sub.end() );
		reverse( s2sub.begin(), s2sub.end() );

		s1 = atoi( s1sub.c_str() );
		s2 = atoi( s2sub.c_str() );
		sum = s1 + s2 + atoi(nasht.c_str());
		string strsu = intToStr(sum);
		reverse( strsu.begin(), strsu.end() );
		while( strsu.length() < len )
			strsu += "0";

		if( strsu.length() > len )
		{
			nasht = strsu.substr( len, 1 );
			strsu = strsu.substr( 0, len );
		}
		else
			nasht = "0";
		strSum += strsu;
		from += len;
		length -= len;
		strsu = "";
	}
}

void incString( string& st )
{
	for( int i = 0; i < st.length(); i++ )
	{
		if( st.substr( st.length() - 1 - i, 1 ) == "2" )
			st.at(st.length() - 1 - i) = '0';
		else if( st.substr( st.length() - 1 - i, 1 ) == "1" )
		{
			st.at(st.length() - 1 - i) = '2';
			break;
		}
		else
		{
			st.at(st.length() - 1 - i) = '1';
			break;
		}
	}
}

void composePar( int digs )
{
	bool odd = digs%2;
	int o = (odd == true) ? 1 : 0;
	int siz = digs/2 + o;
	string nn = "1";
	string dest = "2";
	for( int i = 0; i < siz-1; i++ )			// EDITED
	{
		nn += "0";
		if( i == siz - 2 )
			dest += "2";
		else
			dest += "0";
	}

	while( nn < dest )
	{
		string revNN = "";
		if( odd )
		{
			revNN = nn.substr( 0, nn.length() -1 );
			reverse( revNN.begin(), revNN.end() );
		}
		else
		{
			revNN = nn;
			reverse( revNN.begin(), revNN.end() );
		}
		revNN = nn + revNN;
		if( !checkNumbers(mltp( revNN, revNN )))			// EDITED
			return;
		incString( nn );
	}
}

void topFive( int digs )
{
	string neww[5] = {"1", "2", "3", "11", "22"};

	for( int newwNo = 0; newwNo < 5; newwNo++ )
	{
		digs = neww[newwNo].length();
		bool odd = digs%2;
		int o = (odd == true) ? 1 : 0;
		int siz = digs/2 + o;
		string nn = neww[newwNo];

		string revNN = "";
		if( odd )
		{
			revNN = nn.substr( 0, nn.length() -1 );
			reverse( revNN.begin(), revNN.end() );
		}
		else
		{
			revNN = nn;
			reverse( revNN.begin(), revNN.end() );
		}
		revNN = nn + revNN;
		checkNumbers(mltp( nn, nn ));			// EDITED
	}
}

int main()
{
	for(int i = 0; i < _digs; i++ )
	{
		for(int j = 0; j < i; j++ )
		{
			dd[i][j] = '0';
		}
	}
	for(int i = 0; i < _digs; i++ )
	{
		dd[i][0] = '1';
	}
	int T;
	ifstream inf;
	inf.open("C-small-attempt0.in");
	oufile.open("setText.txt");
	inf >> T;
	string A, B;
	for( int c = 0; c < T; c++ )
	{
		SUMM = 0;
		inf >> A >> B;
		_glba = A;
		_glbb = B;
		_alen = A.length();
		_blen = B.length();

		int lenA = A.length() / 2 - 1;

		topFive( 1 );

		for( int k = 3; k < 10; k++ )
		{
			composePar( k );
		}

		string oup = "";
		stringstream out;
		out << c + 1;
		stringstream ccoutd;
		ccoutd << SUMM;
		oup = "Case #" + out.str() + ": " + ccoutd.str() + "\n"; 
		oufile << oup;

	}



	oufile.close();
	inf.close();

	system("pause");
	return 0;
}

string mltp(string &numString1 ,string &numString2 )
{
	if( numString1.length() == 1 && numString2.length() == 1 )
	{
		return intToStr( atoi(numString1.c_str()) * atoi(numString2.c_str()) );
	}

	string SE ,GE; 

	int LEN=0, diff=0;
	if(numString1.length()<numString2.length())
	{
       LEN=numString1.length();
	   SE=numString1;
	   GE="0"+numString2;
	   diff=numString2.length()-LEN+1;

	}
	else 
	{
		LEN=numString2.length();
        SE=numString2;
		GE="0"+numString1;
		diff=numString1.length()-LEN+1;
	}

 
	string ss;
	string* line =  new string[LEN];
	string nashti="0";

      int a;
      for(int i=LEN-1;i>=0;i--)
	  {	  
		for(int j=LEN+diff-1;j>=0;j--)
		{
            a= atoi(SE.substr (i,1).c_str()) *  atoi(GE.substr (j,1).c_str());

		    ss = intToStr(a);
			
			
            int ff;
			int kk;
			if(ss.length()==1)
			{
			     ff = atoi(ss.c_str())+atoi(nashti.c_str());
				if(intToStr(ff).length()==1)
				{
			      line[i]=line[i]+intToStr(ff);
				  nashti="0";
				}
				else
				{
                   line[i]=line[i]+intToStr(ff).substr (1,1);
				   nashti=intToStr(ff).substr (0,1);
				}
		
			}
			else
			{
                
				kk = atoi(ss.c_str())+atoi(nashti.c_str());
				if(intToStr(kk).length()==1)
				{
			      line[i]=line[i]+intToStr(kk);
				  nashti="0";
				}
				else
				{
                   line[i]=line[i]+intToStr(kk).substr (1,1);
				   nashti=intToStr(kk).substr (0,1);
				}

				
			}
			ss="";
			
		}
	  }




	  for(int c=LEN-1;c>=0;c--)
	  {
        
		  for(int t=0;t<LEN-1-c;t++)
		 {
		    line[c]="0"+line[c] ;
		  }		  

	  }

   


	string sDest ="" , tempst=line[LEN-1];


	int d=0;
    while(d<LEN-1)
	{
      bigSum(sDest,tempst,line[LEN-2-d]);
      tempst=sDest;
	  d++;
	}  

  
	  
     delete[] line;

	 reverse( sDest.begin(), sDest.end());
	 while( sDest.substr(0, 1) == "0" )
		 sDest = sDest.substr( 1, sDest.length() - 1 );

	 return sDest;
}