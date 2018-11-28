#include <iostream>
#include <fstream>
#include <math.h>
using namespace std;
void Impossible(ofstream& outfile,int caseIndex)
{
	outfile << "Case #"<<caseIndex<<":\nImpossible\n";
}
int main()
{
	ifstream infile("C-large.in");
	ofstream outfile("large.out");

	int T,R,C,M;
	infile >> T;
	for (int i = 1 ; i<T+1 ; ++i)
	{
		// debug
		

		infile >> R >>C >> M;
		//outfile << R  <<" " << C << " " << M <<"\n";
		if (min(R,C) == 1)		// ֻ��һ�л�һ��
		{
			int not_m_output;
			int not_m  = R * C -M;
			outfile << "Case #" << i << ":\n";
			for (int k = 0; k < R; k++)
			{
				for(int l =0; l < C; l++)
				{
					if (k == 0 && l==0)
					{ 
						outfile << 'c';
						not_m_output = 1;
						continue;
					}
					if(not_m_output < not_m)
					{
						outfile <<'.';
						not_m_output ++;
					}else
					{
						outfile <<'*';
					}
				}
				outfile << '\n';
			}
			continue;
		}
		else if (min(R,C) == 2)	// ������л�����
		{
			int not_M = R*C - M;
			if (not_M == 1)
			{
				outfile << "Case #" <<i <<":\n";
				outfile<<'c';
				for(int k = 1; k < C; k++)
				{
					outfile <<"*";
				}
				outfile<<"\n";
				for (int l = 1 ; l < R; l++)
				{
					for (int k = 0; k < C; k++)
					{
						outfile << "*";
					}
					outfile<<"\n";
				}
				continue;
			}else if (not_M == 2 || (not_M % 2 ==1))
			{
				Impossible(outfile,i);
				continue;
			}
			else
			{
				outfile << "Case #" << i << ":\n";
				if (C == 2) // 2 ��
				{
					int m_row = M/2;
					for (int l = 0; l < m_row; l++)
					{
						outfile <<"**\n";
					}
					for (int l = m_row ; l < R-1; l++)
					{
						outfile <<"..\n";
					}
					// ���һ��
					outfile <<".c\n";
				}
				else //  2 ��
				{
					int m_col = M/2;
					for (int k = 0; k<m_col;k++)
					{
						outfile << "*";
					}
					for (int k = m_col; k<C; k++)
					{
						outfile <<".";
					}
					outfile << '\n';
					for (int k = 0; k<m_col;k++)
					{
						outfile << "*";
					}
					for (int k = m_col; k<C-1; k++)
					{
						outfile <<".";
					}
					outfile << "c\n";
				}
			}
		}
		else // r,c >=2			// ������������������
		{
			int not_M = R *C -M; // �����׵�����
			if (not_M < 9)		// ����С��9���񣬿��ܲ�����
			{
				switch (not_M)
				{
				case 2:case 3:case 5:case 7:
					Impossible(outfile,i);continue;
				case 1: // ֻ��һ������
					{
						outfile << "Case #" << i << ":\n";
						outfile << 'c';// click pos
						for (int k = 1; k <C ; k++)
						{
							outfile <<'*';
						}
						outfile <<'\n'; //��һ�н���
						for (int l = 1; l <R; l++)
						{
							for (int k = 0; k < C; k++)
							{
								outfile <<'*';
							}
							outfile <<'\n';
						}

						continue;
						break;
					}
				case 4: // ֻ��4������
					{
						outfile << "Case #" << i << ":\n";
						outfile<< 'c' << '.';
						for (int k = 2; k<C;k++)
						{
							outfile << '*';
						}
						outfile <<'\n';
						outfile <<"..";
						for (int k = 2; k<C;k++)
						{
							outfile << '*';
						}
						outfile <<'\n';
						for(int l = 2; l< R; l++)
						{
							for (int k = 0; k<C; k++)
							{
								outfile <<'*';
							}
							outfile <<'\n';
						}
						continue;
						break;
					}
				case 6: // ֻ��6������
					{
						outfile << "Case #" << i << ":\n";

						outfile << "c..";
						for (int k = 3; k< C; k++)
						{
							outfile <<'*';
						}
						outfile << '\n';
						outfile << "...";
						for (int k = 3; k< C; k++)
						{
							outfile <<'*';
						}
						outfile << '\n';
						for (int l = 2;l < R; l++)
						{
							for (int k = 0; k<C; k++)
							{
								outfile << '*';
							}
							outfile <<'\n';
						}
						continue;
						break;
					}
				case 8: //8������
					{
						outfile << "Case #" << i << ":\n";
						outfile << "c..";
						for (int k = 3; k< C; k++)
						{
							outfile <<'*';
						}
						outfile << '\n';
						outfile <<"...";
						for (int k = 3; k< C; k++)
						{
							outfile <<'*';
						}
						outfile << '\n';
						outfile <<"..*";
						for (int k = 3; k< C; k++)
						{
							outfile <<'*';
						}
						outfile << '\n';
						for (int l = 3;l < R; l++)
						{
							for (int k = 0; k<C; k++)
							{
								outfile << '*';
							}
							outfile <<'\n';
						}
						continue;
						break;
					}

				}
			}else	//���� >= 9���ǿ��е�
			{
				outfile << "Case #" << i << ":\n";
				int OR = M/C;
				int OC = M - OR * C;
				int CRE = C - OC;
				int RR = R - OR;
				if (RR >3)// ʣ�� > 4 ����
				{
					if(CRE ==1 ) // ��Ҫ����
					{
						for (int l = 0; l < OR; l++)
						{
							for (int k = 0; k< C; k++)
							{
								outfile <<"*";
							}
							outfile <<'\n';
						}
						for (int k = 0; k < OC -1; k++)
						{
							outfile <<"*";
						}
						outfile <<"..\n";
						outfile<<"*";
						for (int k = 1; k< C; k++)
						{
							outfile <<".";
						}
						outfile <<"\n";

						// ��ʣ�� RR-1��

						for (int l = 0; l < RR-2-1; l++)
						{
							for (int k =0; k< C; k++)
							{
								outfile <<".";
							}
							outfile<<'\n';
						}

						for (int k = 0; k < C-1; k++)
						{
							outfile <<".";
						}
						outfile << 'c' << '\n';
					}
					else // ����Ҫ����
					{
						for (int l = 0; l< OR ; l++)
						{
							for (int k = 0; k<C; k++)
							{
								outfile << "*";
							}
							outfile <<'\n';
						}
						for (int k = 0; k < OC; k++)
						{
							outfile <<"*";
						}
						for (int k = 0; k < CRE; k++)
						{
							outfile <<".";
						}
						outfile <<"\n";

						for(int l = 0; l <RR-1-1; l++)
						{
							for (int k =0; k<C; k++)
							{
								outfile << ".";
							}
							outfile <<"\n";
						}

						for (int k = 0; k < C-1; k++)
						{
							outfile <<".";
						}
						outfile << 'c' << '\n';
					}
					continue;
					break;
				}
				else 
				{
					RR = 3;
					OR = R - RR;
					int mine_remain = M - OR * C;
					int last_col = mine_remain/3;
					int last_last = mine_remain - last_col *3;
					switch(last_last)
					{
					case 0:
						{
							// ��ǰ�����е���
							for (int l = 0; l < OR ; l++)
							{
								for (int k = 0; k<C; k++)
								{
									outfile << "*";
								}
								outfile << '\n';
							}
							for (int l = 0; l < RR -1 ; l++)
							{
								for (int k = 0; k < last_col ; k++)
								{
									outfile <<"*";
								}
								for (int k = 0; k < C-last_col; k++)
								{
									outfile <<".";
								}
								outfile <<"\n";
							}

							// ���һ�� ��c
							for (int k = 0; k < last_col ; k++)
							{
								outfile <<"*";
							}
							for (int k = 0; k < C-last_col-1; k++)
							{
								outfile <<".";
							}
							outfile <<"c";
							outfile <<"\n";
							continue;
							break;
						}
					case 1:
						{
							for (int l = 0; l < OR ; l++)
							{
								for (int k = 0; k<C; k++)
								{
									outfile << "*";
								}
								outfile << '\n';
							}
							for (int k =0; k< last_col + 1; k++)
							{
								outfile <<"*";
							}
							for (int k = 0; k < C-last_col -1; k++)
							{
								outfile << ".";
							}
							outfile <<"\n";
							for (int l = 0; l< 1; l++)
							{
								for (int k = 0; k < last_col ; k++)
								{
									outfile <<"*";
								}
								for (int k = 0; k < C-last_col; k++)
								{
									outfile <<".";
								}
								outfile <<"\n";
							}
							// ���һ����c
							for (int k = 0; k < last_col ; k++)
							{
								outfile <<"*";
							}
							for (int k = 0; k < C-last_col-1; k++)
							{
								outfile <<".";
							}
							outfile <<"c";
							outfile <<"\n";

							continue;
							break;
						}
					case 2:
						{
							{
								for (int l = 0; l < OR ; l++)
								{
									for (int k = 0; k<C; k++)
									{
										outfile << "*";
									}
									outfile << '\n';
								}
								for (int k =0; k< last_col + 2; k++)
								{
									outfile <<"*";
								}
								for (int k = 0; k < C-last_col -2; k++)
								{
									outfile << ".";
								}
								outfile <<"\n";
								for (int l = 0; l< 1; l++)
								{
									for (int k = 0; k < last_col ; k++)
									{
										outfile <<"*";
									}
									for (int k = 0; k < C-last_col; k++)
									{
										outfile <<".";
									}
									outfile <<"\n";
								}
								// ���һ����c
								for (int k = 0; k < last_col ; k++)
								{
									outfile <<"*";
								}
								for (int k = 0; k < C-last_col-1; k++)
								{
									outfile <<".";
								}
								outfile <<"c";
								outfile <<"\n";
								continue;
								break;
							}
						}
					}
				}
			}

		}


















	}
}