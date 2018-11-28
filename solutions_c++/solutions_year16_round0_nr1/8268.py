/*
 *	Counting Sheep - Versão 1.0
 *	Desenvolvido por: Nelson Carvalho de Morais Junior
 *	Email: nelson.carvalho1303@gmail.com
 *	Data: 09-04-2016
 *	Local: Cotia, São Paulo, Brasil
 */
# include <stdio.h>
# include <stdlib.h>
# include <string.h>

int main () {
	// Arquivos entrada / saída
	FILE *fileInput;
	FILE *fileOutput;
	// Declaração de variáveis
	int T, N;					// Entrada númerica
	char strN[7];				// Conversão de número em string
	int vFlag[11], vN[7];		// Vetores
	int a, b, c, d;				// Contadores
	int Sleep;					// Flag
	// Leitura de arquivos
	fileInput = fopen ("A-large.in", "r");
	fileOutput = fopen ("A-large.out", "w");
	// Obter iterações
	fscanf (fileInput, "%d", &T);
	// Início das iterações
	for (a = 0; a < T; a ++){
		// Obter valor N e converter para string
		fscanf (fileInput, "%d", &N);
		itoa (N, strN, 10);
		// Zerar flag vFlag
		for (b = 0; b < 10; b ++) {
			vFlag[b] = 0;
		}
		// Zerar flag Sleep e contadores c e d
		Sleep = 0;
		c = 1;
		d = N;
		// Laço para verificar quando dormir
		while (Sleep == 0) {
			// Converter string para vetor
			for (b = 0; b < 10; b ++) {
				vN[b] = strN[b] - 48;
				// Se o valor da conversão não for um algarismo (fora do intervalo 0 ~ 9), armazena valor negativo para que o valor não apareça no cálculo
				if (vN[b] < 0 || vN[b] > 9) {
					vN[b] = 10;
				}
			}
			// Identificar algarismos do valor N
			for (b = 0; b < 10; b ++) {
				vFlag[vN[b]] = 1;
			}
			// Considerar Sleep como verdadeiro, para realizar as comparações
			Sleep = 1;
			// Caso haja um algarismo que não apareceu, mudar Sleep para 0
			for (b = 0; b < 10; b ++) { 
				if (vFlag[b] == 0) {
					Sleep = 0;
				}
			}
			// Caso Sleep for falso, preparar variáveis para reiniciar o processo. Caso Sleep for 1, preparar variáveis para saída de dados
			if (Sleep == 0) {
				// Obter novo valor para teste e convertê-lo para string
				c ++;
				d = N * c;
				// Se o valor se repetir, loop infinito - não dorme
				if (d == N) {
					fprintf (fileOutput, "Case #%d: INSOMNIA\n",a + 1);
					Sleep = 1;
				}
				itoa (d, strN, 10);
			} else {
				fprintf (fileOutput, "Case #%d: %d\n",a + 1 , d);
			}
		}
	}
	// Fim das iterações	
	return 0;
}
