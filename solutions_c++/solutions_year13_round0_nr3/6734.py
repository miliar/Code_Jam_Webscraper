#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
using namespace std;
/********ȫ�ֱ���***********/
int length = 0, c = 0;
//�����޸ģ�A
int maxnum = (int)sqrt(1000);

/*********����**********/

bool palindrome(char *s, int c)
{
	if (c >= length-c-1)
		return 1;
	if (s[c] == s[length - 1 - c]){
		return palindrome(s, c+1);
	}
	return 0;

}

/*********main����**********/
int main()
{
freopen("D:\\kubox\\OJ\\HDU\\2013google\\C-small-attempt1.in","r",stdin);//�����ض����������ݽ���in.txt�ļ��ж�ȡ
freopen("D:\\kubox\\OJ\\HDU\\2013google\\out.txt","w",stdout);//����ض���������ݽ�������out.txt�ļ���
int line;
int a, b, res=0;
//�����޸�,A
char dp[1100] = {0};
//�����޸ģ�A
char tmp[1100];


cin >> line;

for (int i = 0; i <= maxnum; ++i) {
	sprintf(tmp,"%d",i);
	length = strlen(tmp);
	if (palindrome(tmp, c))
		dp[i * i] = '1';
}


for(int i=1; i<=line; i++)
{
	cin >> a >> b;
	res = 0, length = 0;
	for (int k = a; k <= b; ++k) {
		if (dp[k] == '1'){
//			cout << k << " " << dp[k] << endl;
			sprintf(tmp,"%d",k);
			length = strlen(tmp);
			c = 0;
			if (palindrome(tmp, c)) {
				res ++;
//				cout << k << " " << '2' << endl;
			}
			c = 0;
		
		
		}
	}


	cout << "Case #" << i << ": " << res << endl;
}



fclose(stdin);//�ر��ļ�   
fclose(stdout);//�ر��ļ� 

// system("pause");
    return 0;
}

