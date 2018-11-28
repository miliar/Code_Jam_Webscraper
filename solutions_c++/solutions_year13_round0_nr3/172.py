#include <iostream>
#include <string>
#include <cstring>
using namespace std;

class Num
{
public:
	Num()
	{
		memset(digit,0,sizeof(digit));
		length = 0;
	}
	Num(string s)
	{
		memset(digit,0,sizeof(digit));
		length = s.size();
		for(int i=0;i<length;i++)
		{
			digit[i] = s[length-i-1] - '0';
		}
	}
	int digit[200];
	int length;
};

bool operator<(const Num& a, const Num& b)
{
	if(a.length < b.length)
		return true;
	else if(a.length > b.length)
		return false;
	int size = a.length;
	for(int i=size-1;i>=0;i--)
	{
		if(a.digit[i] < b.digit[i]) return true;
		else if(a.digit[i] > b.digit[i]) return false;
	}
	return false;
}

bool operator==(const Num& a, const Num& b)
{
	if(a.length != b.length) return false;
	for(int i=0;i<a.length;i++)
		if(a.digit[i] != b.digit[i]) return false;
	return true;
}

Num operator*(const Num& a, const Num& b)
{
	Num temp;
	for(int i=0;i<a.length;i++)
	{
		for(int j=0;j<b.length;j++)
		{
			temp.digit[i+j] += a.digit[i] * b.digit[j];
			temp.digit[i+j+1] += temp.digit[i+j]/10;
			temp.digit[i+j] %= 10;
		}
	}
	temp.length = a.length + b.length - 1;
	while(temp.digit[temp.length]) temp.length++;
	while(temp.digit[temp.length - 1] >= 10)
	{
		temp.digit[temp.length] += temp.digit[temp.length-1] / 10;
		temp.digit[temp.length-1] %= 10;
		temp.length++;
	}
	return temp;
}

Num operator+(const Num& a, const Num& b)
{
	Num temp;
	for(int i=0;i<a.length || i<b.length;i++)
	{
		if(i<a.length) temp.digit[i] += a.digit[i];
		if(i<b.length) temp.digit[i] += b.digit[i];
		temp.digit[i+1] += temp.digit[i] / 10;
		temp.digit[i] %= 10;
	}
	temp.length = a.length > b.length? a.length : b.length;
	while(temp.digit[temp.length])
	{
		temp.digit[temp.length+1] += temp.digit[temp.length] / 10;
		temp.digit[temp.length] %= 10;
		temp.length++;
	}
	return temp;
}

Num operator+(const Num& a, int b)
{
	Num temp = a;
	temp.digit[0] += b;
	for(int i=0;i<temp.length;i++)
	{
		if(temp.digit[i] >= 10)
		{
			temp.digit[i+1] += temp.digit[i]/10;
			temp.digit[i] %= 10;
		}
		else if(temp.digit[i] < 0)
		{
			temp.digit[i+1] -= 1;
			temp.digit[i] += 10;
		}
	}
	while(temp.digit[temp.length])
	{
		temp.digit[temp.length+1] += temp.digit[temp.length] / 10;
		temp.digit[temp.length] %= 10;
		temp.length++;
	}
	while(temp.length > 1 && temp.digit[temp.length-1] == 0)
		temp.length--;
	return temp;
}

Num operator/(const Num& a, int b)
{
	Num temp;
	temp.length = a.length;
	int sum = 0;
	for(int i=a.length-1; i>=0; i--)
	{
		sum *= 10;
		sum += a.digit[i];
		temp.digit[i] = sum / b;
		sum %= b;
	}
	while(temp.length > 1 && temp.digit[temp.length-1] == 0)
		temp.length--;
	if(sum) temp = temp+1;
	return temp;
}

Num sqrt(const Num& a)
{
	Num high = a;
	Num low;
	low.length = 1;
	low.digit[0] = 1;
	while(low < high)
	{
		Num mid = (low + high);
		mid = mid / 2;
		Num mid2 = mid * mid;
		if(mid2 < a)
		{
			low = mid;
		}
		else if(a < mid2)
		{
			high = mid + (-1);
		}
		else
			return mid;
	}
	return low;
}

long long C(int a, int b)
{
	if(b>a) return 0;
	if(b==0 || b==a) return 1;
	if(a-b < b) b = a-b;
	long long result = 1;
	for(int i=1;i<=b;i++)
	{
		result*=a+1-i;
		result/=i;
	}
	return result;
}

long long cal(int i)
{
	if(i==1)
		return 3;
	long long result = 0;
	if(i%2)
	{
		int half = (i-3)/2;
		result += C(half,3) + C(half,2) + C(half,1) + C(half,0);
		result += 1;
		result *= 2;
		result += C(half,1) + C(half,0);
	}
	else
	{
		int half = i/2 - 1;
		result += C(half,3) + C(half,2) + C(half,1) + C(half,0);
		result++;
	}
	return result;
}

long long dfs(Num& a, const Num& std, int maximum, const int& len, const int& maxlen, int index)
{
	if(index >= maxlen)
	{
		if(a < std) return 1;
		else return 0;
	}
	long long result = 0;
	if(maximum)
	{
		a.digit[index] = a.digit[len - index - 1] = 1;
		result += dfs(a,std,maximum-1,len,maxlen,index+1);
	}
	a.digit[index] = a.digit[len - index - 1] = 0;
	result += dfs(a,std,maximum,len,maxlen,index+1);
	return result;
}

long long solve(const Num& a)
{
	if(a.length == 1)
	{
		if(a.digit[0] == 0) return 0;
		else if(a.digit[0] < 4) return 1;
		else if(a.digit[0] < 9) return 2;
		else if(a.digit[0] <= 9) return 3;
	}
	Num sqrta = sqrt(a);
	Num temp = sqrta * sqrta;
	while(temp < a || temp == a)
	{
		sqrta = sqrta + 1;
		temp = sqrta * sqrta;
	}
	long long result = 0;
	for(int i=1;i<sqrta.length;i++)
		result += cal(i);
	temp = Num();
	temp.length = sqrta.length;
	if(temp.length == 1)
	{
		if(sqrta.digit[0] <= 1) return 0;
		else if(sqrta.digit[0] == 2) return 1;
		else if(sqrta.digit[0] == 3) return 2;
		else if(sqrta.digit[0] >= 4) return 3;
	}
	if(temp.length % 2)
	{
		temp.digit[temp.length / 2] = 0;
		temp.digit[0] = temp.digit[temp.length-1] = 2;
		if(temp < sqrta) result++;
		temp.digit[0] = temp.digit[temp.length-1] = 1;
		result += dfs(temp,sqrta,3,temp.length,temp.length/2,1);
		temp = Num();
		temp.length = sqrta.length;
		temp.digit[temp.length / 2] = 1;
		temp.digit[0] = temp.digit[temp.length-1] = 2;
		if(temp < sqrta) result++;
		temp.digit[0] = temp.digit[temp.length-1] = 1;
		result += dfs(temp,sqrta,3,temp.length,temp.length/2,1);
		temp = Num();
		temp.length = sqrta.length;
		temp.digit[temp.length / 2] = 2;
		temp.digit[0] = temp.digit[temp.length-1] = 1;
		result += dfs(temp,sqrta,1,temp.length,temp.length/2,1);
		return result;
	}
	else
	{
		temp.digit[0] = temp.digit[temp.length-1] = 2;
		if(temp < sqrta) result++;
		temp.digit[0] = temp.digit[temp.length-1] = 1;
		result += dfs(temp,sqrta,3,temp.length,temp.length/2,1);
	}
	return result;
}

int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		string a,b;
		cin >> a >> b;
		//cout << "Test: " << a << " " << b << endl;
		Num A(a), B(b);
		long long result = 0;
		cout << "Case #" << c << ": ";
		long long sb = solve(B);
		long long sa = solve(A + (-1));
		cout << sb - sa << endl;
	}
}