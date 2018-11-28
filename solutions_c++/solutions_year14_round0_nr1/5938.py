#include <stdio.h>

int m_numberOfCases;
int m_caseNumber;
int m_gridOne[16];
int m_gridTwo[16];
int m_gridOneRow, m_gridTwoRow;
int m_possibleAnswers[4];
int m_numberOfAnswers;

int main(void) {
	FILE *outputFile, *inputFile;
	fopen_s(&inputFile, "A-small-attempt2.in", "r");
	fopen_s(&outputFile, "solution.txt", "w");

	fscanf_s(inputFile, "%i", &m_numberOfCases);

	m_caseNumber = 1;
	while( m_numberOfCases > 0 ) {
		m_numberOfAnswers = 0;
		fscanf_s(inputFile, "%i", &m_gridOneRow);
		for (int i = 0; i < 16; i += 4) {
			fscanf_s(inputFile, "%i %i %i %i", &(m_gridOne[i]), &(m_gridOne[i + 1]), &(m_gridOne[i + 2]), &(m_gridOne[i + 3]));
		}
		fscanf_s(inputFile, "%i", &m_gridTwoRow);
		for (int i = 0; i < 16; i += 4) {
			fscanf_s(inputFile, "%i %i %i %i", &(m_gridTwo[i]), &(m_gridTwo[i + 1]), &(m_gridTwo[i + 2]), &(m_gridTwo[i + 3]));
		}

		for (int j = 0; j < 4; j++) {
			m_possibleAnswers[j] = m_gridOne[m_gridOneRow*(4 - 1) + j];
		}

		unsigned char answerOne, answerTwo;
		for (int i = 0; i < 4; i++) {
			answerOne = m_gridOne[((m_gridOneRow - 1) * 4) + i];
			for (int j = 0; j < 4; j++) {
				answerTwo = m_gridTwo[((m_gridTwoRow - 1) * 4) + j];
				if (answerOne == answerTwo) {
					m_possibleAnswers[m_numberOfAnswers] = answerOne;
					m_numberOfAnswers++;
				}
			}
		}

		if (m_numberOfAnswers == 0) {
			fprintf_s(outputFile, "Case #%i: Volunteer cheated!\n", m_caseNumber);
		}
		else if (m_numberOfAnswers == 1) {
			fprintf_s(outputFile, "Case #%i: %u\n", m_caseNumber, m_possibleAnswers[0]);
		}
		else {
			fprintf_s(outputFile, "Case #%i: Bad magician!\n", m_caseNumber);
		}

		m_caseNumber++;
		m_numberOfCases--;
	}


	fclose(outputFile);
	fclose(inputFile);
}