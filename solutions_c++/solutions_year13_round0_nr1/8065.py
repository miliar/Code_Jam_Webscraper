#include <iostream>
#include <string>

const int QTD_CASAS = 4;

bool ProcuraVencedorLinhas(char* szResult, char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	for (int i = 0; i < QTD_CASAS; i++)
	{
		char cJogador = pJogo[i][0];
		if(cJogador == '.')
			continue;
		bool bVenceu = true;
		for (int j = 1; j < QTD_CASAS; j++)
		{
			if(cJogador != pJogo[i][j])
			{
				if(pJogo[i][j] != 'T')
				{
					bVenceu = false;
					break;
				}
			}
		}

		if(bVenceu)
		{
			sprintf_s(szResult, 1024, "%c won", cJogador);
			return true;
		}
	}

	return false;
}

bool ProcuraVencedorColunas(char* szResult, char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	for (int i = 0; i < QTD_CASAS; i++)
	{
		char cJogador = pJogo[0][i];
		if(cJogador == '.')
			continue;
		bool bVenceu = true;
		for (int j = 1; j < QTD_CASAS; j++)
		{
			if(cJogador != pJogo[j][i])
			{
				if(pJogo[j][i] != 'T')
				{
					bVenceu = false;
					break;
				}
			}
		}

		if(bVenceu)
		{
			sprintf_s(szResult, 1024, "%c won", cJogador);
			return true;
		}
	}

	return false;
}

bool ProcuraVencedorDiagonalPrincipal(char* szResult, char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	char cJogador = pJogo[0][0];
	if(cJogador == '.')
		return false;
	bool bVenceu = true;
	for (int i = 1; i < QTD_CASAS; i++)
	{
		if(cJogador != pJogo[i][i])
		{
			if(pJogo[i][i] != 'T')
			{
				bVenceu = false;
				break;
			}
		}
	}

	if(bVenceu)
		sprintf_s(szResult, 1024, "%c won", cJogador);

	return bVenceu;
}

bool ProcuraVencedorDiagonalSecundaria(char* szResult, char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	char cJogador = pJogo[QTD_CASAS - 1][0];
	if(cJogador == '.')
		return false;
	bool bVenceu = true;
	for (int i = 1; i < QTD_CASAS; i++)
	{
		int pos = QTD_CASAS -1 -i;

		if(cJogador == 'T')
		{
			cJogador = pJogo[pos][i];
			continue;
		}

		if(cJogador != pJogo[pos][i])
		{
			if(pJogo[pos][i] != 'T')
			{
				bVenceu = false;
				break;
			}
		}
	}

	if(bVenceu)
		sprintf_s(szResult, 1024, "%c won", cJogador);

	return bVenceu;
}

bool JogoEstaCompleto(char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	for (int i = 0; i < QTD_CASAS; i++)
	{
		for (int j = 0; j < QTD_CASAS; j++)
		{
			if(pJogo[i][j] == '.')
				return false;
		}
	}

	return true;
}

void ProcuraVencedor(char* szResult, char pJogo[QTD_CASAS][QTD_CASAS + 1])
{
	if(ProcuraVencedorLinhas(szResult, pJogo))
		return;
	if(ProcuraVencedorColunas(szResult, pJogo))
		return;
	if(ProcuraVencedorDiagonalPrincipal(szResult, pJogo))
		return;
	if(ProcuraVencedorDiagonalSecundaria(szResult, pJogo))
		return;

	if(JogoEstaCompleto(pJogo))
		sprintf_s(szResult, 1024, "Draw");
	else
		sprintf_s(szResult, 1024, "Game has not completed");
}

int main()
{
	char jogo[QTD_CASAS][QTD_CASAS + 1] = { 0 };

	int qtdRepeticoes = 0;
	std::cin >> qtdRepeticoes;

	std::string output;

	for(int i = 0; i < qtdRepeticoes; i++)
	{
		for (int j = 0; j < QTD_CASAS; j++)
		{
			std::cin >> jogo[j];
		}

		char temp[1024] = { 0 };
		char result[1024] = { 0 };
		ProcuraVencedor(result, jogo);
		sprintf_s(temp, "Case #%d: %s", i + 1, result);

		output += temp;
		output += "\n";
	}

	std::cout << output << std::endl;

	return 0;
}