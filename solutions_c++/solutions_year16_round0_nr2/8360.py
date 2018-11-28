/*
 *	Revenge of the Pancakes - Vers�o 1.0
 *	Desenvolvido por: Nelson Carvalho de Morais Junior
 *	Email: nelson.carvalho1303@gmail.com
 *	Data: 09-04-2016
 *	Local: Cotia, S�o Paulo, Brasil
 */
# include <stdio.h>
# include <stdlib.h>
# include <string.h>
// Prot�tipos de fun��o
void Inverte (char str[100], int qtde);
int VerificaSmile (char str[100]);
int main () {
	// Arquivos entrada/sa�da
	FILE *fileInput;
	FILE *fileOutput;
	// Declara��o de vari�veis
	int T;					// Entrada - Itera��es
	char S[1000];			// Entrada - String +/-
	int F;					// Sa�da - Flip
	int a, b;				// Contadores
	int fSmile, fContinua;	// Flags
	// Leitura de arquivos
	fileInput = fopen ("B-large.in", "r");
	fileOutput = fopen ("B-large.out", "w");
	// Obter itera��es
	fscanf (fileInput, "%d", &T);
	for (a = 0; a < T; a ++) {
		fscanf (fileInput, "%s", S);
		// Zerar quantidade de Flip
		F = 0;
		// Verificar Smile
		fSmile = VerificaSmile (S);
		while (fSmile == 0) {
			// Zerar flag Continua e contador b
			fContinua = 1;
			b = 1;
			// Obter intervalos de valores repetidos da string S
			while (fContinua == 1) {
				if (S[0] == S[b]) {
					b ++;
				} else {
					fContinua = 0;		
				}
			}
			Inverte (S, b);
			// Incrementar Flips
			F ++;
			fSmile = VerificaSmile (S);
		}
		fprintf (fileOutput, "Case #%d: %d\n", a + 1, F);
	}
	return 0;
}
// Fun��o para inverter panquecas
void Inverte (char str[100], int qtde) {
	// Vari�veis contador e auxiliar
	int i, aux;
	aux = 1;
	// Obter o per�odo repetido de +/- e inverter o sinal para -/+
	for (i = 0; i < qtde; i ++) {
		if (str[i] == '+') {
			str[i] = '-';
		} else {
			str[i] = '+';
		}
	}
}
// Fun��o para verificar se os rostos das panquecas est�o para cima ou para baixo
int VerificaSmile (char str[100]) {
	int i;
	// Verificar todos os valores da string, se achar algum valor -, retorna 0 para continuar os Flips
	for (i = 0; i < 100; i ++) {
		if (str[i] == '-') {
			return 0;
		}
	}
	return 1;
}
