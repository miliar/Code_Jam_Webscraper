#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>

using namespace std;


const int DIGITS = 15;
char dd[DIGITS][DIGITS] = { '0' };
ofstream oufile;
int SUMM = 0;
int Alen;
int Blen;
string glA;
string glB;



string arr[100];
int gli=0;



class TT{

public:
	string multiply(string &numString1 ,string &numString2 );
    bool	ifPalindr( string(& str) );
	bool checkNumb( string &stst, string &stsmall );
	void sumStrs( string(& strSum), string(& str1), string(& str2) );
	void incStr( string& st );
	void printNumsLess( int digs );
	void printNums( int digs );

};


bool TT::ifPalindr( string(& str) )
{
	bool pali = true;
	int len = str.length();

	for( int i = 0; i <= len / 2 && pali; i++ )
		pali *= (str.substr(i, 1) == str.substr( len - 1 - i, 1 )) ? true : false;

	return pali;
}

bool TT::checkNumb( string &stst, string &stsmall )
{
	if( ifPalindr(stst) )
	{
		arr[gli]=stst;
		gli++;
		/*int LLL = stst.length();
		if( LLL > Alen && LLL < Blen )
		{
			SUMM++;
		    cout << stst << "    " << stsmall << endl;
		}
		else if( LLL > Blen )
		{
			return false;
		}
		else
		{
			if( LLL == Alen && LLL == Blen && stst >= glA && stst <= glB )
			{
				SUMM++;
				cout << stst << "    " << stsmall << endl;
			}
			else if( LLL == Alen && LLL != Blen && stst >= glA )
			{
				SUMM++;
				cout << stst << "    " << stsmall << endl;
			}
			else if( LLL != Alen && LLL == Blen && stst <= glB )
			{
				SUMM++;
				cout << stst << "    " << stsmall << endl;
			}

		} */
	}
	return true;
}

string intToStr( int k )
{
	stringstream ss;
	ss << k;
	return ss.str();
}

void TT::sumStrs( string(& strSum), string(& str1), string(& str2) )
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

void incrChar( int len, char(& ch)[DIGITS] )
{
	for( int i = 0; i < len; i++ )
	{
		if( ch[len - 1 - i] == '9' )
			ch[len - 1 - i] = '0';
		else
		{
			ch[len - 1 - i] = ch[len - 1 - i] + 1;
			break;
		}
	}
}

void TT::incStr( string& st )
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

void TT::printNums( int digs )
{
	bool odd = digs%2;
	int o = (odd == true) ? 1 : 0;
	int siz = digs/2 + o;
	string nn = "1";
	string dest = "2";
	for( int i = 0; i < siz-1; i++ )			
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
		if( !checkNumb(multiply( revNN, revNN ), revNN))		
			return;
		incStr( nn );
	}
}

void TT::printNumsLess( int digs )
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
		checkNumb(multiply( nn, nn ), nn);			
	}
}



string TT::multiply(string &numString1 ,string &numString2 )
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
	   //GE=numString2;
	   GE="0"+numString2;
	   diff=numString2.length()-LEN+1;

	}
	else 
	{
		LEN=numString2.length();
        SE=numString2;
        //GE=numString1;
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
      sumStrs(sDest,tempst,line[LEN-2-d]);
      tempst=sDest;
	  d++;
	}  

  
	  
     delete[] line;

	 reverse( sDest.begin(), sDest.end());
	 while( sDest.substr(0, 1) == "0" )
		 sDest = sDest.substr( 1, sDest.length() - 1 );

	 return sDest;
}

int main()
{
	
	TT obj;
	

	
	for(int i = 0; i < DIGITS; i++ )
	{
		for(int j = 0; j < i; j++ )
		{
			dd[i][j] = '0';
		}
	}
	for(int ii = 0; ii < DIGITS; ii++ )
	{
		dd[ii][0] = '1';
	}
	int T;
	ifstream inf;
	inf.open("C-large-1.in");
	oufile.open("out.txt");
	inf >> T;
	string A, B;
	

	obj.printNumsLess( 1 );
		

		for( int k = 3; k < 10; k++ )
		{
			obj.printNums( k );
			
		}




	for( int c = 0; c < T; c++ )			
	{
		SUMM = 0;
		inf >> A >> B;
		glA = A;
		glB = B;
		Alen = A.length();
		Blen = B.length();

		int lenA = A.length() / 2 - 1;
	
//////////////////////////////////////////////////////

		for(int tt=0;tt<gli ;tt++)
		{
            int LLL = arr[tt].length();
			string stst=arr[tt];
			if( LLL > Alen && LLL < Blen )
			{
			  SUMM++;
			}
			else if( LLL > Blen )
			{
			   break;
			}
		    else
			{
			  if( LLL == Alen && LLL == Blen && stst >= glA && stst <= glB )
			  {
				SUMM++;
			  }
			  else if( LLL == Alen && LLL != Blen && stst >= glA )
			  {
				SUMM++;
			  }
			  else if( LLL != Alen && LLL == Blen && stst <= glB )
			  {
				SUMM++;
			  }

		} 


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

