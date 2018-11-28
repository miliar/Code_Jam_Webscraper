#include <stdio.h>

// ����true��ʾ���ֱ�ʤ
bool slove(unsigned int x,unsigned int r,unsigned int c)
{
	unsigned int count = r*c;
	if(1 == x) return false;
	if(2 == x) return (0 != (count&1));
	if(3 == x)
	{
		if(1 == r || 1 == c) return true;			// ��
		if(0 != (count%3)) return true;
		return false;								// ������һ����3,����һ�����ڵ���2ʱ,�����ۿ��Թ���2*3,ʣ�µ�������
	}
	if(4 == x)
	{
		if(1 == r || 1 == c) return true;			// ����
		if(r < 4 && c < 4) return true;				// ����
		if(0 != (count%4)) return true;
		// ������һ��Ϊ4
		if(2 == r || 2 == c) return true;			// ͹��
		return false;
	}
	return true;
}

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int x = 0,r = 0,c = 0;scanf("%d%d%d",&x,&r,&c);
		bool ans = slove(x,r,c);
		printf("Case #%u: %s\n",iCases,ans?"RICHARD":"GABRIEL");
	}
	return 0;
}