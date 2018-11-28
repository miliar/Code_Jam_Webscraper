#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
using namespace std;
int equ, var; 
int a[26][11];
int x[10]; 
bool free_x[10]; 
int free_num;


//template part

int gcd(int a,int b)
{
    int t;
    while(b!=0)
    {
        t=b;
        b=a%b;
        a=t;
    }
    return a;
}
int lcm(int a,int b)
{
    return a/gcd(a,b)*b;//�ȳ���˷����
}

// ��˹��Ԫ���ⷽ����(Gauss-Jordan elimination).(-2��ʾ�и������⣬���������⣬
//-1��ʾ�޽⣬0��ʾΨһ�⣬����0��ʾ����⣬���������ɱ�Ԫ�ĸ���)
//��equ�����̣�var����Ԫ�������������Ϊequ,�ֱ�Ϊ0��equ-1,����Ϊvar+1,�ֱ�Ϊ0��var.
int Gauss(int equ,int var)
{
    int i,j,k;
    int max_r;// ��ǰ���о���ֵ������.
    int col;//��ǰ�������
    int ta,tb;
    int LCM;
    int temp;
    int free_x_num;
    int free_index;

    for(int i=0;i<=var;i++)
    {
        x[i]=0;
        free_x[i]=true;
    }

    //ת��Ϊ������.
    col=0; // ��ǰ�������
    for(k = 0;k < equ && col < var;k++,col++)
    {// ö�ٵ�ǰ�������.
// �ҵ���col��Ԫ�ؾ���ֵ�����������k�н���.(Ϊ���ڳ���ʱ��С���)
        max_r=k;
        for(i=k+1;i<equ;i++)
        {
            if(abs(a[i][col])>abs(a[max_r][col])) max_r=i;
        }
        if(max_r!=k)
        {// ���k�н���.
            for(j=k;j<var+1;j++) swap(a[k][j],a[max_r][j]);
        }
        if(a[k][col]==0)
        {// ˵����col�е�k������ȫ��0�ˣ�����ǰ�е���һ��.
            k--;
            continue;
        }
        for(i=k+1;i<equ;i++)
        {// ö��Ҫɾȥ����.
            if(a[i][col]!=0)
            {
                LCM = lcm(abs(a[i][col]),abs(a[k][col]));
                ta = LCM/abs(a[i][col]);
                tb = LCM/abs(a[k][col]);
                if(a[i][col]*a[k][col]<0)tb=-tb;//��ŵ���������
                for(j=col;j<var+1;j++)
                {
                    a[i][j] = a[i][j]*ta-a[k][j]*tb;
                }
            }
        }
    }

  //  Debug();

    // 1. �޽�����: ������������д���(0, 0, ..., a)��������(a != 0).
    for (i = k; i < equ; i++)
    { // �����������˵�����Ҫ�ж���Щ�����ɱ�Ԫ����ô�����б任�еĽ����ͻ�Ӱ�죬��Ҫ��¼����.
        if (a[i][col] != 0) return -1;
    }
    // 2. ���������: ��var * (var + 1)���������г���(0, 0, ..., 0)�������У���˵��û���γ��ϸ����������.
    // �ҳ��ֵ�������Ϊ���ɱ�Ԫ�ĸ���.
    if (k < var)
    {
        // ���ȣ����ɱ�Ԫ��var - k��������ȷ���ı�Ԫ������var - k��.
        for (i = k - 1; i >= 0; i--)
        {
            // ��i��һ��������(0, 0, ..., 0)���������Ϊ�����������ڵ�k�е���equ��.
            // ͬ������i��һ��������(0, 0, ..., a), a != 0��������������޽��.
            free_x_num = 0; // �����жϸ����еĲ�ȷ���ı�Ԫ�ĸ������������1�������޷���⣬������ȻΪ��ȷ���ı�Ԫ.
            for (j = 0; j < var; j++)
            {
                if (a[i][j] != 0 && free_x[j]) free_x_num++, free_index = j;
            }
            if (free_x_num > 1) continue; // �޷�����ȷ���ı�Ԫ.
            // ˵����ֻ��һ����ȷ���ı�Ԫfree_index����ô���������ñ�Ԫ���Ҹñ�Ԫ��ȷ����.
            temp = a[i][var];
            for (j = 0; j < var; j++)
            {
                if (a[i][j] != 0 && j != free_index) temp -= a[i][j] * x[j];
            }
            x[free_index] = temp / a[i][free_index]; // ����ñ�Ԫ.
            free_x[free_index] = 0; // �ñ�Ԫ��ȷ����.
        }
        return var - k; // ���ɱ�Ԫ��var - k��.
    }
    // 3. Ψһ������: ��var * (var + 1)�����������γ��ϸ����������.
    // �����Xn-1, Xn-2 ... X0.
    for (i = var - 1; i >= 0; i--)
    {
        temp = a[i][var];
        for (j = i + 1; j < var; j++)
        {
            if (a[i][j] != 0) temp -= a[i][j] * x[j];
        }
        if (temp % a[i][i] != 0) return -2; // ˵���и������⣬����������.
        x[i] = temp / a[i][i];
    }
    return 0;
}
// end template


int N;
char* words[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE",
			   "SIX", "SEVEN", "EIGHT", "NINE"};

void init(){
	memset(a, 0, sizeof(a));
	for(int i=0;i<10; ++i){
		char* ptr = words[i];
		for(int j = 0;ptr[j]; ++j){
			++a[ptr[j] - 'A'][i];
		}
	}
}
int main(void) {
	cin>>N;
	char str[2003];
	for(int cs = 1; cs<= N; ++cs){
		cin>>str;
		init();
		memset(x, 0, sizeof(x));
		memset(free_x, 1, sizeof(free_x)); // һ��ʼȫ�ǲ�ȷ���ı�Ԫ.
		for(int i= 0; str[i]; ++i){
			++a[str[i]-'A'][10];
		}
		// for(int i=0;i<26;++i){
		// 	for(int j=0;j<11;++j){
		// 		cout<<a[i][j]<<' ';
		// 	}
		// 	cout<<endl;
		// }
		int res =Gauss(26, 10);
		// cout<<res<<endl;
		cout<<"Case #"<<cs<<": ";
		for(int i=0; i< 10; ++i){
			while(x[i]--){
				cout<<i;
			}
		}
		cout<<endl;
		
	}
	return 0;
}
