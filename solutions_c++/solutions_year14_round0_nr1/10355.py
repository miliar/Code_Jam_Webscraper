#include<iostream>
using namespace std;
int main()
{
	freopen("A-small-attempt2.in","r",stdin); //�����ض����������ݽ���in.txt�ļ��ж�ȡ
	freopen("output.txt","w",stdout); //����ض���������ݽ�������out.txt�ļ���

	int nCount =  0;			//�Աȵ�����
	cin>>nCount;		
	int nPreSaves[4];			//������Ӧ��ֵ
	int nPreBufs[4];			//������Ӧ��ֵ
	int nSelectRowCount = 0;    //ѡ�������
	int nSameNum = 0;			//���Ƶ�����
	int nSame = 0;				//���Ƶ���
	for (int i = 0 ; i < nCount ; i++)
	{
		nSameNum = 0;
		cin>>nSelectRowCount;
		nSelectRowCount--;
		for (int j = 0; j < 4; j++)
		{
			if (j == nSelectRowCount)
			{
				cin>>nPreSaves[0]>>nPreSaves[1]>>nPreSaves[2]>>nPreSaves[3];
			}
			else
			{
				cin>>nPreBufs[0]>>nPreBufs[1]>>nPreBufs[2]>>nPreBufs[3];
			}
		}

		cin>>nSelectRowCount;
		nSelectRowCount--;
		for (int j = 0; j < 4 ; j++)
		{
			cin>>nPreBufs[0]>>nPreBufs[1]>>nPreBufs[2]>>nPreBufs[3];

			if (j == nSelectRowCount)
			{
				for (int k = 0 ; k < 4 ; k++)
				{
					for (int p = 0 ; p < 4 ; p++)
					{
						if (nPreBufs[p] == nPreSaves[k])
						{
							nSameNum++;
							nSame = nPreSaves[k];
							break;
						}
					}
				}
			}	
		}
		cout<<"Case #"<<i+1<<": ";
		switch(nSameNum)
		{
		case 0:
			cout<<"Volunteer cheated!"<<endl;
			break;
		case 1:
			cout<<nSame<<endl;
			break;
		default:
			cout<<"Bad magician!"<<endl;
		}
	}
//	fclose(stdin);//�ر��ļ�
	fclose(stdout);//�ر��ļ�
	return 0;
}



