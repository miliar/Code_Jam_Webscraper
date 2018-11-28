#include <iostream>
#include <string>
#include <cmath>
using namespace std;

double pi = acos(-1.0);

//�Ǹ����Ƚ�
bool Less(string &x, string &y){	return x.size()<y.size() || x.size()==y.size()&&x<y;	}

//�Ǹ�����ǰ��0
void Head_zero_remove(string &x)
{
	if(x[0]!='0')	return ;
	x.erase(0,x.find_first_not_of('0'));
	if(x.empty())	x="0";
}

//�Ǹ������
string Add(string x, string y)
{
	if(x.size()<y.size())	x.swap(y);						//x�ĳ���<y�ĳ���
	y.insert(y.begin(), x.size()-y.size(), '0');			//y��0����
	string sum(x.size(),-1);									//��ʼ��С��x.size()
	int carry=0;
	for(int i=x.size()-1; i>=0; i--)
		if((carry+=x[i]+y[i]-96)>9)	sum[i]=char(carry-10+48), carry=1;
		else		sum[i]=char(carry+48), carry=0;
	if(carry)	return '1'+sum;
	else	return sum;
}

//�Ǹ���������������Ϊ��
string Minus(string x, string y)
{
	bool neg=0;						//���Ϊ�����
	if(Less(x,y))		x.swap(y),neg=1;
	y.insert(y.begin(), x.size()-y.size(), '0');		//y��0����
	string diff(x.size(),-1);								//�����ֵ��
	int carry=0;					//��λ���
	for(int i=x.size()-1; i>=0; i--)
		if(x[i]>=y[i]+carry)	diff[i]=x[i]-y[i]-carry+'0', carry=0;
		else					diff[i]=x[i]+10-y[i]-carry+'0', carry=1;
	Head_zero_remove(diff);
	if(neg)		return '-'+diff;
	else		return diff;
}

//�Ǹ��߾��ȳ˵;���
string Multiply(string s, int a)
{
	if(s=="0" || a==0)		return "0";
	string prod(s.size(),-1);				//������s.size()λ
	int carry=0;
	for(int i=s.size()-1; i>=0; i--)	carry+=(s[i]-'0')*a, prod[i]=carry%10+'0', carry/=10;
	while(carry)	prod.insert(prod.begin(),carry%10+'0'), carry/=10;
	return prod;
}

//�Ǹ��߾��ȳ˸߾���
string Multiply(string x, string y)
{
	string prod="0";
	for(int i=y.size()-1; i>=0; i--)
	{
		string p_sum= Multiply(x,y[i]-'0');
		if(p_sum!="0")	p_sum.insert(p_sum.end(), y.size()-1-i, '0');
		prod = Add(prod, p_sum);
	}
	return prod;
}

//�Ǹ��߾��ȳ��Ե;��ȣ�������Ϊ0��
string Divide(string x, int y, int &remainder)
{
	string quotient(x.size(),0);
	remainder=0;
	for(int i=0; i<x.size(); i++)
		remainder=remainder*10+x[i]-'0', quotient[i]=remainder/y+'0', remainder%=y;
	Head_zero_remove(quotient);
	return quotient;			//remainder��Ϊ���������
}

//�Ǹ��߾��ȳ��Ը߾��ȣ�������Ϊ0��
string Divide(string x, string y, string &remainder)
{
	string quotient(x.size(),'0');
	remainder="";				//��ʼΪ�ո�ÿ������һ���ַ�
	for(int i=0; i<x.size(); i++)
	{
		remainder+=x[i];
		while(!Less(remainder,y))	remainder=Minus(remainder,y),quotient[i]++;		//����>���������������������̼�1
	}
	Head_zero_remove(quotient);			
	return quotient;			//remainderΪ����
}

//�Ǹ��߾��ȵĵ;�����
string Power(string s, int a)
{
	string power="1";
	while(a)	power=(a&1)?Multiply(power,s):power, a>>=1, s=Multiply(s,s);
	return power;
}

//�Ǹ��߾��ȿ�ƽ��
string Sqrt(string s)
{
	string ret((s.size()+1)>>1, -1);
	string res=s.substr(0,2-(s.size()&1)), div="0";		//res��λȡǰ1��żλȡǰ2�� divռһλ��
	for(int i=0; i<ret.size(); i++)
		for(int quot=9; ;quot--)
		{
			div[div.size()-1]=quot+'0';				//ĩβ���̣���9��0
			string p_prod=Multiply(div, quot);
			if(!Less(res,p_prod))
			{
				ret[i]=quot+'0';					//�����׷�ӣ�
				div=Multiply(ret.substr(0,i+1),20);		
				res=Minus(res, p_prod);
			
				string nxt2=s.substr(((i+1)<<1)-(s.size()&1),2);
				if(res=="0")	res=nxt2;		//ȡ��2λ
				else	res+=nxt2;				//����2λ��׷�ӣ���res = res*100+next2
				break;
			}
		}
	return ret;				//��ʱres��Ϊ����
}

//**************�����Ǹ���֧��*******************************************

//ȡ�෴������������
string Neg(string s)
{
	if(s[0]=='-')		return s.substr(1,s.size()-1);
	if(s=="0")			return s;
	return '-'+s;
}

//�ӷ�����������
string SAdd(string x, string y)
{
	if(x[0]=='-'&&y[0]=='-')	return Neg(Add(Neg(x),Neg(y)));
	if(x[0]=='-')				return Minus(y,Neg(x));
	if(y[0]=='-')				return Minus(x,Neg(y));
	return Add(x,y);
}

//��������������
string SMinus(string x, string y)
{
	if(x[0]=='-'&&y[0]=='-')	return Minus(Neg(y),Neg(x));
	if(x[0]=='-')				return Neg(Add(Neg(x),y));
	if(y[0]=='-')				return Add(x,Neg(y));
	return Minus(x,y);
}

//�߾��ȳ˵;��ȣ���������
string SMultiply(string s, int a)
{
	if(s[0]=='-'&&a<0)			return Multiply(Neg(s),-a);
	if(s[0]=='-')				return Neg(Multiply(Neg(s),a));
	if(a<0)						return Neg(Multiply(s,-a));
	return Multiply(s,a);
}

//�߾��ȳ˸߾��ȣ���������
string SMultiply(string x, string y)
{
	if(x[0]=='-'&&y[0]=='-')	return Multiply(Neg(x),Neg(y));
	if(x[0]=='-')				return Neg(Multiply(Neg(x),y));
	if(y[0]=='-')				return Neg(Multiply(x,Neg(y)));
	return Multiply(x,y);
}

int main ()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;		scanf("%d", &tc);
	for (int T = 1; T <= tc; T++)
	{
		//double r, t;	scanf("%lf%lf", &r, &t);
		//double a = 2, b = -1.0 + 2 * r, c = - t; //cout << b << endl;
		//double n = (- b + sqrt(b * b - 4 * a * c)) / (2 * a);
		////double n = - b / (2.0 * a) + sqrt( (b / a) * (b / a) / 4 - c / a);
		////double n = sqrt((r/2) * (r/2) + t/2 - r/4) - (r/2 - 1/4);
		//int ans = floor(n);
		////printf("%lf, %lf, %lf, %lf\n",a, b, c, n);
		//printf("Case #%d: %d\n", T, ans);

		string r, t;	cin >> r >> t;
		string a = "2", b = SAdd("-1", Multiply("2", r)), c = Neg(t);
		int tem1;
		string ans1 = Divide(b, 4, tem1);
		if (tem1 == 0)
			ans1 = Neg(ans1);
		else
			ans1 = Neg(Add(ans1, "1"));

		string tem2 = SMinus(Multiply(b, b), SMultiply("4", SMultiply(a, c)));

		//cout << tem2;
		int tem;
		string root = Divide(tem2, 16, tem);
		//cout << " " << "16" << " " << root << endl << endl << endl;;
		string ans2 = Sqrt(root);
		string ans = SAdd(ans1, ans2);
		//cout << a << " " << b << " " << c << " "  << " "<< tem << " " <<ans <<" " <<  root << " " <<endl;
		//cout << ans1 << " " << ans2 <<" " << ans << endl;

		while (1)
		{
			string newans = Add(ans, "1");
			string newtem = SAdd(c, SAdd(SMultiply(b, newans), SMultiply(a, SMultiply(newans, newans))));
			//cout << "while: " << newans << " " << newtem << endl;
			if (newtem[0] == '-' || newtem[0] == '0')	ans = newans;
			else	break;
		}
		cout << "Case #" << T << ": " << ans << endl;

	}
}