#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <set>

using namespace std;

template <typename type>
type intSqrt (type remainder, type* _remainder)
{
  if (remainder < 0)
	return 0; 

  type place = (type)1 << (sizeof (type) * 8 - 2); 
  while (place > remainder)
	place /= 4; 

  type root = 0;
  while (place)
  {
	if (remainder >= root+place)
	{
	  remainder -= root+place;
	  root += place * 2;
	}
	root /= 2;
	place /= 4;
  }
  *_remainder = remainder;
  return root;
}

string radix(string _num, short* remainder)
{
	*remainder=0;
	string num = _num;
	while(*(num.begin())=='0')
		num.erase(0,1);

	int _size = num.length();
	short num_buf, r;
	char buf[3];
	const char* c_str = num.c_str();
	string result;

	if(_size<=2)
	{
		//num_buf=(c_str[0]-'0')*10 + c_str[1]-'0';
		num_buf = atoi(c_str);
		short v = intSqrt(num_buf, remainder);
		//short v2 = v*v;
		//if(v2 < num_buf)
		//	*remainder=num_buf-v2;
		_itoa(v,buf,10);
		result.append(buf);
		return result;
	}

	if(_size%2)
		num.insert(0,"0");

	r=0;
	unsigned long p = 0;
	unsigned long y,yn;
	int dp1;
	for(int i=0; i<num.size(); i+=2)
	{
		buf[0] = c_str[i];
		buf[1] = c_str[i+1];
		num_buf = atoi(buf);
		
		
		
		yn = r*100+num_buf;
		dp1=0;
		do
		{
			dp1++;
			y = dp1*(20*p+dp1);
		}
		while(y<=yn);
		dp1--;
		y = dp1*(20*p+dp1);
		if(dp1!=0)
		{
			_itoa(dp1,buf,10);
			result += (buf);
		}
		//r -= y;
		//r = num_buf - y;
		p=p*10 + dp1;
		r = yn - y;
		//y=num_buf;
	}
	

	*remainder = r;
	return result;
}

bool checkPalindrome(string str)
{
	int mid = str.length() / 2;
	stack<char> stc;
	int i;
	for(i=0;i<mid;i++)
		stc.push(str[i]);

	i += str.length() % 2;
	for(; i<str.length(); i++)
	{
		char ch = stc.top();
		if(ch!=str[i])
			return false;
		stc.pop();
	}

	while(!stc.empty())
		stc.pop();

	return true;
}

string incstr(string X)
{
	int len = X.length();
	string res=X;
	char c=0;
	len--;

	do
	{
		if(c==0)
		{
			c = res[len]-47;
			c %= 10;
			res[len--] = c+48; 
			
		}
		else 
			break;
	}while((len>=0));

	if((c==0)&&(len<0))
		res.insert(0,"1");


	return res;
	
}


bool fairAndSquare(string X)
{
	string radix_X;
	
	if(!checkPalindrome(X))
		return false;
	
	
	double d = atof(X.c_str());
	unsigned long u = (unsigned long) d;
	unsigned long r=0;
	unsigned long v = intSqrt(u, &r);
	if(r>0)
		return false;
	char buf[1000];
	_ltoa(v,buf,10);
	radix_X=buf;
	if(!checkPalindrome(radix_X))
		return false;
	
	/*
	short rem=0;
	string _radix_X = radix(X,&rem);
	if(rem>0)
		return false;
	if(!checkPalindrome(_radix_X))
		return false;
		*/
	return true;
}

int computeResult(string A, string B)
{
	int count=0;
	string X = A;
	while(X!=B)
	{
		count+=fairAndSquare(X);
		X=incstr(X);
	}
	count+=fairAndSquare(X);	
	return count;
}



void main(int argc, char* argv[])
{
	int T;
	string str;
	string::iterator si;
	ifstream ifile;
	

	if(argc<=1)
		ifile.open("../example.in");
	else
		ifile.open(argv[1]);
	if(!ifile.is_open())
	{
		cout << "File not Found! in " << endl; 
		exit(-1);
	}
	
	ifile >> T;
	string A,B;
	for(int t=1; t<=T; t++)
	{
		ifile >> A >> B;
		int result = computeResult(A,B);	
		cout << "Case #" << t << ": " << result << endl;
	}

	ifile.close();
}